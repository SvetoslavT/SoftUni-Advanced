from custom_exeptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

# Exercise 2 (Email-Validator)
domains = ['com', 'bg', 'org', 'net']

while True:
    command = input().split("@")

    if len(command) != 2:
        raise MustContainAtSymbolError("Email must contain @")
    name = command[0]
    full_domain = command[1]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    full_domain_explode = full_domain.split(".")
    if len(full_domain_explode) != 2:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    domain_name = full_domain_explode[0]
    domain = full_domain_explode[1]
    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
