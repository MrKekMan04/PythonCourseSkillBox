import json

with open("json_old.json", "r", encoding="UTF-8") as json_old_file:
    old_json = dict(json.load(json_old_file))

with open("json_new.json", "r", encoding="UTF-8") as json_new_file:
    new_json = dict(json.load(json_new_file))

diff_list = {"services", "staff", "datetime"}


def get_a(old: dict, new: dict, diffs: dict):
    for key in old.keys():
        if key in old and key in new:
            if type(old[key]) is dict and type(new[key]) is dict:
                get_a(old[key], new[key], diffs)
            else:
                if key in diff_list and old[key] != new[key]:
                    diffs[key] = new[key]


diffs = {}
get_a(old_json, new_json, diffs)
print(diffs)

with open("result.json", "w", encoding="UTF-8") as file:
    json.dump(diffs, file, ensure_ascii=False, indent=4)
