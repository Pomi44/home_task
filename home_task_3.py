import argparse
from functools import partial
from multiprocessing import Pool


def find(path, keyword):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return keyword in file.read()
    except FileNotFoundError:
        print("Файл не найден")
    except:
        print("Ошибка при открытии файла")


if __name__ == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', dest="keyword")
    parser.add_argument('-p', '--paths', nargs='+', dest="paths")
    argv = parser.parse_args()
    with Pool(5) as p:
        print(p.map(partial(find, keyword=argv.keyword), argv.paths)) 