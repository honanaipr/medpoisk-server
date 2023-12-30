def flatten_divisions(S):
    if not S:
        return S
    return S[:1] + flatten_divisions(S[0].sub_divisions) + flatten_divisions(S[1:])
