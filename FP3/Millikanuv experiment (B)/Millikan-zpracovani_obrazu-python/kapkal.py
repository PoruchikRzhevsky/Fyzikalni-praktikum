from time import sleep
import numpy as np
import pandas as pd
from drops_filter import DropsData, DropsFilter
from matplotlib import pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("video_files", type=str, nargs="+",
                        help="Path to video files")
    parser.add_argument("--fit-std-threshold", type=float, default=0.1,
                        help="Standard deviation threshold when fitting drops speed (default: 0.1))")
    parser.add_argument("-s", "--speed", type=float, default=1,
                        help="Interval between plots in seconds (0 to disable, default: 1))")
    parser.add_argument("--smooth-factor", type=int, default=4,
                        help="Smooth factor for y values (default: 4)))")
    parser.add_argument("-f", "--min-fit-frames", type=int, default=7,
                        help="To fit drops speed, succesful fit on at least this many data points is required (default: 5)")
    parser.add_argument("-o", "--inversion-offset", type=int, default=2,
                        help="How many frames from inversion frame will the y fit start at (default: 2)")
    parser.add_argument("-x", "--x-std-threshold", type=float, default=6,
                        help="Standard deviation threshold for x values (default: 10)")
    parser.add_argument("--save-plots", action="store_true",
                        help="Save plots to pdf files")
    args = parser.parse_args()
    speed = args.speed
    video_files = args.video_files
    fit_std_threshold = args.fit_std_threshold
    smooth_factor = args.smooth_factor
    min_fit_frames = args.min_fit_frames
    inversion_offset = args.inversion_offset
    x_std_threshold = args.x_std_threshold
    save_plots = args.save_plots
    total_drops = 0
    drops_filter = DropsFilter(fit_std_threshold, x_std_threshold, min_fit_frames, inversion_offset)

    plt.figure()
    for video_file in video_files:
        print("Processing", video_file)
        df_x = pd.read_csv(f"{video_file}_x.csv", header=None)
        frames = df_x[0].values
        x = df_x.drop(0, axis=1).values

        df_y = pd.read_csv(f"{video_file}_y.csv", header=None)
        frames = df_y[0].values
        y = df_y.drop(0, axis=1).values

        vy = np.diff(y, axis=0)
        plt.clf()
        plt.xlabel("Frame")
        plt.ylabel("Y")
        plt.plot(frames, y)
        plt.show(block=False)
        if speed > 0:
            plt.pause(speed)

        drops_data = DropsData(frames=frames, x=x, y=y, vy=vy)
        drops_data = drops_filter.smooth_y(
            drops_data, smooth_factor=smooth_factor)

        plt.cla()
        plt.plot(drops_data.frames, drops_data.y)
        plt.show(block=False)
        if speed > 0:
            plt.pause(speed)

        # filtered_drops = drops_filter.apply_x_std_filter(drops_data)

        # plt.cla()
        # plt.plot(filtered_drops.frames, filtered_drops.y)
        # plt.show(block=False)
        # if speed > 0:
        #     plt.pause(speed)
        filtered_drops = drops_data

        inversion_frame, filtered_drops = drops_filter.find_drops_inversion_frame(
            filtered_drops, diff_frame_count=smooth_factor)

        plt.cla()
        plt.plot(filtered_drops.frames, filtered_drops.y)
        plt.show(block=False)
        if speed > 0:
            plt.pause(speed)

        drops = drops_filter.analyze_drops(
            filtered_drops,
            inversion_frame
        )

        # plt.clf()
        # plt.plot(filtered_drops.frames, filtered_drops.y)
        plt.axvline(inversion_frame, color="red", linestyle="--")
        plt.show(block=False)
        if speed > 0:
            plt.pause(speed)
        # Lock plot ax limits
        ax = plt.gca()
        ax.set_ylim(ax.get_ylim())
        ax.set_xlim(ax.get_xlim())
        for drop in drops:
            plt.plot(filtered_drops.frames[:inversion_frame], drop.vy1 * filtered_drops.frames[:inversion_frame] +
                     drop.intercept1, color="green", linestyle="--", linewidth=1)
            plt.plot(filtered_drops.frames[inversion_frame:], drop.vy2 * filtered_drops.frames[inversion_frame:] +
                     drop.intercept2, color="green", linestyle="--", linewidth=1)
        plt.xlabel("Frame")
        plt.ylabel("Y [px]")
        if save_plots:
            plt.savefig(f"{video_file}_plot.pdf")
        plt.show(block=False)
        if speed > 0:
            plt.pause(speed)

        # Save measured drops data
        drops_df = pd.DataFrame()
        drops_df["v1"] = [drop.vy1 for drop in drops]
        drops_df["v2"] = [drop.vy2 for drop in drops]
        drops_df.to_csv(f"{video_file}_drops.csv", index=False)

        print("Drops:", len(drops))
        total_drops += len(drops)

    print("Total drops found:", total_drops)
    print("Filtered - x std:", drops_filter.filtered_x_std_count)
    print("Filtered - fit std:", drops_filter.filtered_min_fit_frames_count)
