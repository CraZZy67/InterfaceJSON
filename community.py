from string import ascii_letters, digits
from json import load, dump
from random import shuffle


class Community:
    def __init__(self, json_file: str):
        with open(json_file) as f:
            self.__content = load(f)

    def add_post(self, title: str, continue_link: str) -> str:
        self.__content[self.gen_link_and_id()[0]] = [title, self.gen_link_and_id()[1], continue_link]
        return title

    def gen_link_and_id(self) -> list:
        list_chars = list()
        for i in str(ascii_letters + digits): list_chars.append(i)

        shuffle(list_chars)
        if "".join(list_chars[0:6]) in self.__content["id_list"]:
            shuffle(list_chars)

        id_ = "".join(list_chars[0:6])
        self.__content["id_list"].append(id_)
        return [id_, f"https://vk.com/im?sel=-226581842&id={id_}"]

    def delete_post(self, id_: str) -> str:
        try:
            if self.check_content():
                self.__content.pop(id_)
                return id_
            else:
                return "Список постов пуст"
        except KeyError as ex:
            return f"Не правильный id поста: {ex}"

    def get_post_link(self, id_: str, type_: str) -> str:
        if self.check_content():
            if type_ == "id":
                return self.__content[id_][1]
            else:
                return self.__content[id_][2]
        else:
            return "Список постов пуст"

    def get_list_posts(self) -> str:
        if self.check_content():
            str_list = ""
            for i, k in self.__content.items():
                if i == "id_list":
                    break
                str_list += f"{i}: {k[0]} | {k[1]} | {k[2]}\n"

            return str_list
        else:
            return "Список постов пуст"

    def check_content(self):
        if len(self.__content) >= 2:
            return True
        else:
            return False

    def save_to_json(self):
        with open('posts.json', 'w') as f:
            dump(self.__content, f, indent=4)
