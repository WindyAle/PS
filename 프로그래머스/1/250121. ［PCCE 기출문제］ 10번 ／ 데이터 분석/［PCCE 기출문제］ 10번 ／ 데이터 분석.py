def solution(data, ext, val_ext, sort_by):
    ext_dict = {e: i for i, e in enumerate(["code", "date", "maximum", "remain"])}
    return sorted([d for d in data if d[ext_dict[ext]] < val_ext], key=lambda x: x[ext_dict[sort_by]])