from playwright.sync_api import Page
from pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # title type filter
    __TITLE_TYPE = {
        "movie": '[data-testid="test-chip-id-movie"]',
        "tvSeries": '[data-testid="test-chip-id-tvSeries"]',
        "short": '[data-testid="test-chip-id-short"]',
        "tvEpisode": '[data-testid="test-chip-id-tvEpisode"]',
        "tvMiniSeries": '[data-testid="test-chip-id-tvMiniSeries"]',
        "tvMovie": '[data-testid="test-chip-id-tvMovie"]',
        "tvSpecial": '[data-testid="test-chip-id-tvSpecial"]',
        "tvShort": '[data-testid="test-chip-id-tvShort"]',
        "video": '[data-testid="test-chip-id-video"]',
        "videoGame": '[data-testid="test-chip-id-videoGame"]',
        "musicVideo": '[data-testid="test-chip-id-musicVideo"]',
        "podcastSeries": '[data-testid="test-chip-id-podcastSeries"]',
        "podcastEpisode": '[data-testid="test-chip-id-podcastEpisode"]',
    }
    #Release date filter
    __RELEASE_DATE_EXPEND = '[aria-label="Expand Release date"]'
    __FROM_DATE = '.jMYOmN [aria-label="Enter release date above"]'
    __TO_DATE = '.jMYOmN [aria-label="Enter release date below"]'
    # Imdb ratings
    __IMDB_RATINGS_EXPEND = '[aria-label="Expand IMDb ratings"]'
    __RATING_MIN = '[name="imdb-ratings-max-input"]' #develloper mistake in name (it's should be "min")
    __RATING_MAX = '[name="imdb-ratings-min-input"]' #develloper mistake in name (it's should be "max")
    #ganer
    __GENER_EXPEND = '[aria-label="Expand Genre"]'
    __GENRES = {
        "Action": '[data-testid="test-chip-id-Action"]',
        "Adventure": '[data-testid="test-chip-id-Adventure"]',
        "Animation": '[data-testid="test-chip-id-Animation"]',
        "Biography": '[data-testid="test-chip-id-Biography"]',
        "Comedy": '[data-testid="test-chip-id-Comedy"]',
        "Crime": '[data-testid="test-chip-id-Crime"]',
        "Documentary": '[data-testid="test-chip-id-Documentary"]',
        "Drama": '[data-testid="test-chip-id-Drama"]',
        "Family": '[data-testid="test-chip-id-Family"]',
        "Fantasy": '[data-testid="test-chip-id-Fantasy"]',
        "Film-Noir": '[data-testid="test-chip-id-Film-Noir"]',
        "Game-Show": '[data-testid="test-chip-id-Game-Show"]',
        "History": '[data-testid="test-chip-id-History"]',
        "Horror": '[data-testid="test-chip-id-Horror"]',
        "Music": '[data-testid="test-chip-id-Music"]',
        "Musical": '[data-testid="test-chip-id-Musical"]',
        "Mystery": '[data-testid="test-chip-id-Mystery"]',
        "News": '[data-testid="test-chip-id-News"]',
        "Reality-TV": '[data-testid="test-chip-id-Reality-TV"]',
        "Romance": '[data-testid="test-chip-id-Romance"]',
        "Sci-Fi": '[data-testid="test-chip-id-Sci-Fi"]',
        "Short": '[data-testid="test-chip-id-Short"]',
        "Sport": '[data-testid="test-chip-id-Sport"]',
        "Talk-Show": '[data-testid="test-chip-id-Talk-Show"]',
        "Thriller": '[data-testid="test-chip-id-Thriller"]',
        "War": '[data-testid="test-chip-id-War"]',
        "Western": '[data-testid="test-chip-id-Western"]',
    }
    __SEE_RESULTS_BTN = '[data-testid="adv-search-get-results"]'
    __SELECTED_FILTER_CHIPS = '.ipc-chip-list__scroller button'


    # title filters
    def title_types(self, *categories):
        if not categories:
            raise ValueError("At least one category must be provided")

        for category in categories:
            locator = self.__TITLE_TYPE.get(category)
            if not locator:
                raise ValueError(f"Category '{category}' is not supported")
            self.click(locator)

    # release date filter
    def release_date(self,from_date,to_date):
        self.click(self.__RELEASE_DATE_EXPEND)
        self.fill_text(self.__FROM_DATE,from_date)
        self.fill_text(self.__TO_DATE,to_date)

    # ratings filter
    def ratings(self,min,max):
        self.click(self.__IMDB_RATINGS_EXPEND)
        self.fill_text(self.__RATING_MIN,min)
        self.fill_text(self.__RATING_MAX,max)

    # genres filter
    def genres(self, *genres):
        if not genres:
            raise ValueError("At least one genre must be provided")

        for genre in genres:
            locator = self.__GENRES.get(genre)
            if not locator:
                raise ValueError(f"Genre '{genre}' is not supported")
            self.click(locator)

    def see_results_btn(self):
        self.click(self.__SEE_RESULTS_BTN)

    def get_selected_filter_texts(self) -> list[str]:
        return [el.inner_text().strip() for el in self.get_locator(self.__SELECTED_FILTER_CHIPS).all()]



