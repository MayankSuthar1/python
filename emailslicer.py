def email_input():
    email = input("Enter the email you want to slice :- ")

    username = email.split('@')
    domain_tld = username[1].split('.')
    print(f"Username :- {username[0]}")
    print(f"Domain   :- {domain_tld[0]}")
    print(f"Tld      :- {domain_tld[1]}")
email_input()