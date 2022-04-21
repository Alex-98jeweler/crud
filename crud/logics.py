

def get_max(model):
    it = model.objects.all()
    max_seq = max([i.seq for i in it])
    return max_seq


def set_seq(model):
    max_seq = get_max(model)
    return max_seq+1
