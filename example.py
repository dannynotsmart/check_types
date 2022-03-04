from check_types import check_types

@check_types
def shoot_balls(who : str, *, why : str, how : str = "gun"):
    print(f"i have shot {who} because {why}. i shot ball by {how}")

shoot_balls("cat", why = "i don't like")
