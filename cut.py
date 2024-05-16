from lib import split_and_strip, odd, input_type


class Comparison:
    def __init__(self, comparison_string):
        self.comparison_string = comparison_string
        self.var, self.sym, self.val = self._parse(comparison_string)

    def _parse(self, comp_string):
        known_comp_syms = [
            '<=',
            '>=',
            '==',
            '!=',
            '>',
            '<',
        ]
        # breakpoint()
        for sym in known_comp_syms:
            try:
                var, val = split_and_strip(comp_string, sym)
                if input_type(val) == str: val = f"'{val}'"
                return var, sym, val
            except ValueError: continue


class Cut:
    def __init__(self, cut_string) -> None:
        self.cut_string = cut_string
        self.comparisons, self.logic_syms = self._parse(cut_string)

    def _parse(self, cut_string):
        known_delims = [
            '[',
            ']'
        ]
        known_logic_syms = [
            '|~',
            '&~',
            '&',
            '|',
        ]
        try: 
            split_cut_string = split_and_strip(cut_string, known_delims)
        except ValueError:
            split_cut_string = [cut_string]
        assert odd(len(split_cut_string))

        comparisons = [Comparison(i) for i in split_cut_string[0::2]]
        
        try: logic_syms = split_cut_string[1::2]
        except: logic_syms = []
        for sym in logic_syms: 
            assert sym in known_logic_syms, ValueError(f"Cut not recognized: {cut_string}")

        return comparisons, logic_syms