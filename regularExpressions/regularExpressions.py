# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
pattern = r".*@.*\..*" # Your pattern here!
test_email(pattern)


# 模範解答
# pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
# 使用する特殊文字の制限
