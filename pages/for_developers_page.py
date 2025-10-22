from pages.base_page import Page


class ForDevelopersPage(Page):

    def verify_fd_opened(self):
        self.wait_for_url_contains('for-developer')
