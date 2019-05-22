a = {"bobby1":{"company":"imooc"},
     "bobby2": {"company": "imooc2"}
     }
#clear
# a.clear()
# pass
b = a
#copy, 返回浅拷贝
new_dict = a.copy()
print(new_dict)
print(id(a),id(b),id(new_dict))
new_dict["bobby1"]["company"] = "imooc3"
import copy
new_dict2 = copy.deepcopy(a)
print(new_dict2)
new_dict2["bobby1"]["company"] = "imooc3"

print(new_dict)
print(a)


#formkeys
new_list = ["bobby1", "bobby2"]

new_dict = dict.fromkeys(new_list, {"company":"imooc"})

new_dict.update((("bobby","imooc"),))

