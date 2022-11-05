import argparse
import datetime
import re
import sys

TIME_REGEX = "\d:\d\d:\d\d\.\d\d\d"
TIME_LINE_REGEX = "^" + TIME_REGEX + "," + TIME_REGEX + "$"


def main(args_list):
    parser = argparse.ArgumentParser(
        prog="Subtitle-shifter",
        description=
        "Shifts (.sbv) subtitles by the given time. Any overlap is not taken "
        "care of, and should be relatively easy for the caller to handle.",
        epilog="Here is where more help would be.")
    parser.add_argument("input", help="input file")
    parser.add_argument(
        "shift_start", type=str,
        help="shift time in the format used by the sbv file, H:MM:SS.SSS")
    parser.add_argument("shift", type=float, help="shift amount in seconds.")
    parser.add_argument(
        "-o", "--output",
        help="Name for output. If omitted the shift will be appended to the "
             "input file base name.")
    args = parser.parse_args(args_list)
    pivot_time = datetime.datetime.strptime(args.shift_start, "%H:%M:%S.%f")
    delta_time = datetime.timedelta(seconds=args.shift)
    if args.output is None:
        args.output = args.input[:-4] + str(args.shift) + ".sbv"
    with open(args.input) as f:
        insbv = f.read()
    with open(args.output, "w") as f:
        for l in insbv.split("\n"):
            l = match_n_move_times(pivot_time, l, delta_time)
            f.write(l + "\n")


def match_n_move_times(
        pivot_time: datetime,
        l: str,
        delta_time: datetime.timedelta):
    if re.match(TIME_LINE_REGEX, l):
        times = [
            datetime.datetime.strptime(x, "%H:%M:%S.%f")
            for x in l.split(",")]
        if times[0] > pivot_time:
            new_times = [
                (x + delta_time).strftime("%H:%M:%S.%f")[1:-3]
                for x in times]
            l = ",".join(new_times)
    return l


if __name__ == "__main__":
    main(sys.argv[1:])
