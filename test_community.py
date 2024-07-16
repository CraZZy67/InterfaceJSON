from unittest import TestCase, main
from community import Community


class TestCommunity(TestCase):
    test_ex_nothing = Community(json_file={"id_list": []})
    test_ex = Community(json_file={"23f456": ["Парус",
                                              "https://vk.com/friends?section=all",
                                              "https://docs.python.org/3/library/unittest.html"],
                                   "45gj89": ["Яхта",
                                              "https://vk.com/friends?section=all",
                                              "https://docs.python.org/3/library/unittest.html"],
                                   "24gh43": ["Море",
                                              "https://vk.com/friends?section=all",
                                              "https://docs.python.org/3/library/unittest.html"],
                                   "id_list": ["23f456", "45gj89", "24gh43"]})

    def test_adding_post(self):
        self.assertIsInstance(
            self.test_ex.add_post(title="Речка", continue_link="https://www.virustotal.com/gui/home/upload"), str)

    def test_deleting_post(self):
        self.assertEqual(self.test_ex_nothing.delete_post("24gh43"), "Список постов пуст")
        self.assertEqual(self.test_ex.delete_post("23f456"), "23f456")
        self.assertIn("Не правильный id поста:", self.test_ex.delete_post("234566"))

    def test_getting_link(self):
        self.assertEqual(self.test_ex_nothing.get_post_link("24gh43"), "Список постов пуст")
        self.assertIsInstance(self.test_ex.get_post_link("24gh43"), str)

    def test_getting_list(self):
        self.assertEqual(self.test_ex_nothing.get_list_posts(), "Список постов пуст")
        self.assertIsInstance(self.test_ex.get_list_posts(), str)

    def test_checking_content(self):
        self.assertFalse(self.test_ex_nothing.check_content())
        self.assertTrue(self.test_ex.check_content())


if __name__ == "__main__":
    main()
