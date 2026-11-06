from gendiff.formater.to_stylish.builde_lines import build_lines


def to_stylish(diff):
    return "\n".join(["{", *build_lines(diff), "}"])
