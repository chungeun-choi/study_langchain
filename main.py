from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    linked_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/chungeun-choi-202585257/"
    )
    print(linked_data)
