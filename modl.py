import pkg_resources

print("All local install modules in python ")

builtins_modules = pkg_resources.working_set
all_modules = sorted(["%s==%s " % (x.key, x.version)
                      for x in builtins_modules])

for a in all_modules:
    print(a)