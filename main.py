import json

from third_parties.linkedin import scrape_linkedin_profile, scrape_gits_profile

if __name__ == "__main__":
    # linked_data = scrape_linkedin_profile(
    #     linkedin_profile_url="https://www.linkedin.com/in/chungeun-choi-202585257/"
    # )
    # print(linked_data)

    url = "https://gist.githubusercontent.com/chungeun-choi/efdfdb4945025fc1690c4ec9ca0e5972/raw/d4b8e558b3617c7aa6ea8baee1cd787fc49a2de3/choi-chungeun.json"
    gits_data = scrape_gits_profile(url)
    print(gits_data)
