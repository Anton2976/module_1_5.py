immutable_var = 1983, "Anton", 2009, "Vera"
print(immutable_var)
print(immutable_var[0])
print(immutable_var[3])
#immutable_var[0] = "Gleb"
#print(immutable_var)
# кортедж не поддерживает обращение по элементам, применяется в качестве неизменеяемого хранилища.
mutable_list = [1983, "Anton", 2009, "Vera"]
print(mutable_list)
mutable_list[1] = "Ira"
print(mutable_list)
mutable_list.append("Denis")
print(mutable_list)
