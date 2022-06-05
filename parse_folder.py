import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="path to folder")
    parser.add_argument(
        "--path",
        type=str,
        help="path to folder to be passed",
    )
    args = parser.parse_args()
    s = "|{}.|[{}]()|[Link]({})|"
    d = {}  # index:string
    for i in os.listdir(args.path):

        index = int(i.split(".")[0])
        question = i.split(".")[1]
        d[index] = s.format(
            index,
            question,
            os.path.join(
                args.path, str(index) + "." + question.replace(" ", "%20") + ".py"
            ),
        )
    for i in range(1, len(d) + 1):
        print(d[i])
