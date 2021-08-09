# def getvalue(nested_dict, value):
#     """Input: nested dict, value"""
#     for k, v in nested_dict.items():
#         if k == value:  # found value
#             return v
#         elif hasattr(v, 'elements'):   # v is a dict
#             p = getvalue(v.elements, value)  # recursive call
#             if p is not None:
#                 return p
#
#
# def getpath(nested_dict, value, track=None):
#     if track is None:
#         track = []
#     for k, v in nested_dict.items():
#         if k == value:  # found value
#             track.append(k)
#             return track
#         elif hasattr(v, 'items'):   # v is a dict
#             p = getpath(v, value, track)  # recursive call
#             if p is not None:
#                 track.append(k)
#                 return p

def getvalue(nested_dict, value):
    """Input: nested dict, value"""
    for k, v in nested_dict.items():
        if k == value:  # found value
            return v
        elif hasattr(v, 'elements'):   # v is a dict
            p = getvalue(v.elements, value)  # recursive call
            if p is not None:
                return p


def getpath(nested_dict, value, track=None):
    if track is None:
        track = []
    for k, v in nested_dict.items():
        if k == value:  # found value
            track.append(k)
            return track
        elif hasattr(v, 'items'):   # v is a dict
            p = getpath(v, value, track)  # recursive call
            if p is not None:
                track.append(k)
                return p