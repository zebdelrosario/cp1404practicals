"""A small script that prompts the user for a page title or search phrase, then prints the summary of that page."""
import wikipedia


def main():
    """Ask for title or search phrase, and print summary."""
    user_input = input("Enter page title/search phrase: \n>")
    while user_input != "":
        try:
            search_result = wikipedia.page(user_input)
            print(f"Title: {search_result.title}\nSummary: {search_result.summary}\nURL:{search_result.url}")
        except wikipedia.exceptions.DisambiguationError:
            print("Too many potential pages; please enter a more specific page!")
        user_input = input("Enter page title/search phrase: \n>")


main()
