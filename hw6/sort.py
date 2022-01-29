import os, shutil, sys


#--------------------- walk through files and folders -------------------------
def traversing_folders(path):
    list_files = []
    list_dirs = []
    for root, dirs, files in os.walk(path):
        for name in files:
            list_files.append(os.path.join(root, name))
        for name in dirs:
            list_dirs.append(os.path.join(root, name))

    return list_files, list_dirs


#------------------------ rename files ----------------------
def normalize(*args):

    lits_for_el = [',', '?', ' ', '~', '!',
               '@', '#', '$', '%', '^',
               '&', '*', '(', ')', '-',
               '=', '+', ':', ';', '<',
               '>', '\'', '"', '\\', '/',
               '№', '[', ']', '{', '}',
               '—']
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

    TRANS = {}
    for a,b in zip(CYRILLIC_SYMBOLS,TRANSLATION):
        TRANS[ord(a)] = b
        TRANS[ord(a.upper())] = b.upper()

    for i in args:
        s = i.translate(TRANS)
        clear_name = s.translate({ord (i):"_" for i in lits_for_el})

    return clear_name


# --------------------- create new dir -------------------------
def create_new_dir(path):

    if not os.path.exists(path + '\\images'):
        os.mkdir(path + '\\images')
    if not os.path.exists(path + '\\video'):
        os.mkdir(path + '\\video')
    if not os.path.exists(path + '\\audio'):
        os.mkdir(path + '\\audio')
    if not os.path.exists(path + '\\documents'):
        os.mkdir(path + '\\documents')
    if not os.path.exists(path + '\\archives'):
        os.mkdir(path + '\\archives')   


#----------------------- moving files -----------------------
def moving_files(path):
    incorrect_file, full_dirs = traversing_folders(path)

    files_info = {'images': [], 'archives': [], 'documents': [], 'audio': [], 'video': [], 'unknown': set([]), 'known': set([])}

    for file in incorrect_file:
        dir_name = os.path.dirname(file)
        file_name = os.path.splitext(os.path.basename(file))
        f_name = file_name[0]
        file_extention = file_name[-1]
        correct_file_name = normalize(f_name) + file_extention

        image_extention = (".jpeg", ".png", ".jpg", ".svg")
        video_extention = (".avi", ".mp4", ".mov", ".mkv")
        doc_extention = (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx")
        audio_extention = (".mp3", ".ogg", ".wav", ".amr")
        archives_extention = (".zip", ".gz", ".tar")

        try:
            if (path + '\\images') == dir_name or (path + '\\video') == dir_name or \
                (path + '\\audio') == dir_name or (path + '\\documents') == dir_name or (path + '\\archives') == dir_name:
                continue

            if file_extention in image_extention:
                new_path = path + '\\images\\' + correct_file_name
                shutil.move(file, new_path)
                files_info['images'].append(correct_file_name)
                files_info['known'].add(file_extention)
                
            elif file_extention in video_extention:
                    new_path = path + "\\video\\" + correct_file_name
                    shutil.move(file, new_path)
                    files_info['video'].append(correct_file_name)
                    files_info['known'].add(file_extention)

            elif file_extention in doc_extention:
                    new_path = path + '\\documents\\' + correct_file_name
                    shutil.move(file, new_path)
                    files_info['documents'].append(correct_file_name)
                    files_info['known'].add(file_extention)

            elif file_extention in audio_extention:
                    new_path = path + "\\audio\\" + correct_file_name
                    shutil.move(file, new_path)
                    files_info['audio'].append(correct_file_name)
                    files_info['known'].add(file_extention)

            elif file_extention in archives_extention:
                    new_path = path + "\\archives\\" + correct_file_name
                    dir_like_name_archive = path + "\\archives\\" + f_name
                    files_info['archives'].append(correct_file_name)
                    files_info['known'].add(file_extention)
                    try:
                         os.mkdir(dir_like_name_archive)
                    except FileExistsError:
                        pass
                    shutil.unpack_archive(file, dir_like_name_archive, file_extention.replace('.', ''))
                    shutil.move(file, new_path)

            else:
                files_info['unknown'].add(file_extention)

        except FileNotFoundError:
                continue
    
    return files_info


#-----------------delete empty dirs--------------------
def remove_empty_dir(path):

    for dirs in os.listdir(path):
        s = os.path.join(path, dirs)
        if os.path.isdir(s):
            remove_empty_dir(s)
            if not os.listdir(s):
                os.rmdir(s)


def main():
    path = r""
    path = ' '.join(sys.argv[1:])
    if path:
        traversing_folders(path)
        create_new_dir(path)
        print(moving_files(path))
        remove_empty_dir(path) 
    else:
        print("Вы не ввели путь! Попробуйте ещё раз!")


if __name__ == "__main__":
    main()