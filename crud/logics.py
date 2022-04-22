

def get_max(model):
    it = model.objects.all()
    try:
        max_seq = max([i.seq for i in it])
    except ValueError:
        max_seq = 0
    return max_seq


def set_seq(model):
    max_seq = get_max(model)
    return max_seq+1
