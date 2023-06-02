import os

def crawl_directory(directory, exclude_file):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename != exclude_file:
                yield os.path.join(dirpath, filename)

def list_files(directory, crawl=False):
    files = []
    file_extension_count = {}

    if crawl:
        files = list(crawl_directory(directory, os.path.basename(__file__)))
    else:
        files = list(os.scandir(directory))
        files = [entry.name for entry in files if entry.is_file() and entry.name != os.path.basename(__file__)]

    for i, file in enumerate(files, 1):
        print(f'{i}. {os.path.basename(file)}')
        ext = os.path.splitext(file)[-1].lower()
        if ext in file_extension_count:
            file_extension_count[ext] += 1
        else:
            file_extension_count[ext] = 1

    print("\nFile extension count:")
    for ext, count in file_extension_count.items():
        print(f'{ext}: {count}')

def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))

    choice = input("Crawl through all directories (yes/no)? ")

    crawl = False

    if choice.lower() == 'yes':
        crawl = True

    list_files(current_directory, crawl)

if __name__ == "__main__":
    main()
