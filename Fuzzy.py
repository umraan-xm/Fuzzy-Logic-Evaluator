import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


def compute_fuzzy_performance(e1_input, e2_input, p_input):


    VL = "VL"
    L = "L"
    A = "A"
    H = "H"
    VH = "VH"

    VU = "VU"
    U = "U"
    AV = "AV"
    S = "S"
    VS = "VS"

    fail = "fail"
    _pass = "pass"
    good = "good"
    very_good = "very good"
    excellent = "excellent"

    exam1_input = e1_input
    exam2_input = e2_input
    practical_input = p_input

    exam1_marks = ctrl.Antecedent(np.arange(0, 100), "Exam1")
    exam1_marks[VL] = fuzz.trimf(exam1_marks.universe, [0, 0, 25])
    exam1_marks[L] = fuzz.trimf(exam1_marks.universe, [0, 25, 50])
    exam1_marks[A] = fuzz.trimf(exam1_marks.universe, [25, 50, 75])
    exam1_marks[H] = fuzz.trimf(exam1_marks.universe, [50, 75, 100])
    exam1_marks[VH] = fuzz.trimf(exam1_marks.universe, [75, 100, 100])


    exam2_marks = ctrl.Antecedent(np.arange(0, 100), "Exam2")
    exam2_marks[VL] = fuzz.trimf(exam2_marks.universe, [0, 0, 25])
    exam2_marks[L] = fuzz.trimf(exam2_marks.universe, [0, 25, 50])
    exam2_marks[A] = fuzz.trimf(exam2_marks.universe, [25, 50, 75])
    exam2_marks[H] = fuzz.trimf(exam2_marks.universe, [50, 75, 100])
    exam2_marks[VH] = fuzz.trimf(exam2_marks.universe, [75, 100, 100])


    fuzzy1 = ctrl.Consequent(np.arange(0, 100), "Fuzzy1")
    fuzzy1[VU] = fuzz.trimf(fuzzy1.universe, [0, 0, 25])
    fuzzy1[U] = fuzz.trimf(fuzzy1.universe, [0, 25, 50])
    fuzzy1[A] = fuzz.trimf(fuzzy1.universe, [25, 50, 75])
    fuzzy1[S] = fuzz.trimf(fuzzy1.universe, [50, 75, 100])
    fuzzy1[VS] = fuzz.trimf(fuzzy1.universe, [75, 100, 100])



    rule1 = ctrl.Rule(exam1_marks[VL] & exam2_marks[VL], fuzzy1[VU])
    rule2 = ctrl.Rule(exam1_marks[VL] & exam2_marks[L], fuzzy1[VU])
    rule3 = ctrl.Rule(exam1_marks[VL] & exam2_marks[A], fuzzy1[U])
    rule4 = ctrl.Rule(exam1_marks[VL] & exam2_marks[H], fuzzy1[U])
    rule5 = ctrl.Rule(exam1_marks[VL] & exam2_marks[VH], fuzzy1[A])

    rule6 = ctrl.Rule(exam1_marks[L] & exam2_marks[VL], fuzzy1[VU])
    rule7 = ctrl.Rule(exam1_marks[L] & exam2_marks[L], fuzzy1[U])
    rule8 = ctrl.Rule(exam1_marks[L] & exam2_marks[A], fuzzy1[U])
    rule9 = ctrl.Rule(exam1_marks[L] & exam2_marks[H], fuzzy1[A])
    rule10 = ctrl.Rule(exam1_marks[L] & exam2_marks[VH], fuzzy1[A])

    rule11 = ctrl.Rule(exam1_marks[A] & exam2_marks[VL], fuzzy1[U])
    rule12 = ctrl.Rule(exam1_marks[A] & exam2_marks[L], fuzzy1[U])
    rule13 = ctrl.Rule(exam1_marks[A] & exam2_marks[A], fuzzy1[A])
    rule14 = ctrl.Rule(exam1_marks[A] & exam2_marks[H], fuzzy1[S])
    rule15 = ctrl.Rule(exam1_marks[A] & exam2_marks[VH], fuzzy1[S])

    rule16 = ctrl.Rule(exam1_marks[H] & exam2_marks[VL], fuzzy1[U])
    rule17 = ctrl.Rule(exam1_marks[H] & exam2_marks[L], fuzzy1[A])
    rule18 = ctrl.Rule(exam1_marks[H] & exam2_marks[A], fuzzy1[S])
    rule19 = ctrl.Rule(exam1_marks[H] & exam2_marks[H], fuzzy1[S])
    rule20 = ctrl.Rule(exam1_marks[H] & exam2_marks[VH], fuzzy1[VS])

    rule21 = ctrl.Rule(exam1_marks[VH] & exam2_marks[VL], fuzzy1[A])
    rule22 = ctrl.Rule(exam1_marks[VH] & exam2_marks[L], fuzzy1[S])
    rule23 = ctrl.Rule(exam1_marks[VH] & exam2_marks[A], fuzzy1[S])
    rule24 = ctrl.Rule(exam1_marks[VH] & exam2_marks[H], fuzzy1[VS])
    rule25 = ctrl.Rule(exam1_marks[VH] & exam2_marks[VH], fuzzy1[VS])

    rule_list = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                 rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                 rule21, rule22, rule23, rule24, rule25]

    fuzzy1_ctrl = ctrl.ControlSystem(rule_list)

    fuzzy1_analysis = ctrl.ControlSystemSimulation(fuzzy1_ctrl)
    fuzzy1_analysis.input["Exam1"] = np.array(exam1_input)
    fuzzy1_analysis.input["Exam2"] = np.array(exam2_input)
    fuzzy1_analysis.compute()

    fuzzy1_crisp = fuzzy1_analysis.output["Fuzzy1"]

    #fuzzy1_crisp_norm = [x/100 for x in fuzzy1_crisp]
    #print(fuzzy1_crisp_norm)


    practical_marks = ctrl.Antecedent(np.arange(0, 100), "Practicals")
    practical_marks[VL] = fuzz.trimf(practical_marks.universe, [0, 0, 25])
    practical_marks[L] = fuzz.trimf(practical_marks.universe, [0, 25, 50])
    practical_marks[A] = fuzz.trimf(practical_marks.universe, [25, 50, 75])
    practical_marks[H] = fuzz.trimf(practical_marks.universe, [50, 75, 100])
    practical_marks[VH] = fuzz.trimf(practical_marks.universe, [75, 100, 100])

    fuzzy2 = ctrl.Antecedent(np.arange(0, 100), "Fuzzy2")
    fuzzy2[VU] = fuzz.trimf(fuzzy2.universe, [0, 0, 25])
    fuzzy2[U] = fuzz.trimf(fuzzy2.universe, [0, 25, 50])
    fuzzy2[A] = fuzz.trimf(fuzzy2.universe, [25, 50, 75])
    fuzzy2[S] = fuzz.trimf(fuzzy2.universe, [50, 75, 100])
    fuzzy2[VS] = fuzz.trimf(fuzzy2.universe, [75, 100, 100])

    performance = ctrl.Consequent(np.arange(0, 100), "Performance")
    performance[fail] = fuzz.trimf(performance.universe, [0, 0, 25])
    performance[_pass] = fuzz.trimf(performance.universe, [0, 25, 50])
    performance[good] = fuzz.trimf(performance.universe, [25, 50, 75])
    performance[very_good] = fuzz.trimf(performance.universe, [50, 75, 100])
    performance[excellent] = fuzz.trimf(performance.universe, [75, 100, 100])


    p_rule1 = ctrl.Rule(fuzzy2[VU] & practical_marks[VL], performance[fail])
    p_rule2 = ctrl.Rule(fuzzy2[VU] & practical_marks[L], performance[fail])
    p_rule3 = ctrl.Rule(fuzzy2[VU] & practical_marks[A], performance[_pass])
    p_rule4 = ctrl.Rule(fuzzy2[VU] & practical_marks[H], performance[_pass])
    p_rule5 = ctrl.Rule(fuzzy2[VU] & practical_marks[VH], performance[good])

    p_rule6 = ctrl.Rule(fuzzy2[U] & practical_marks[VL], performance[fail])
    p_rule7 = ctrl.Rule(fuzzy2[U] & practical_marks[L], performance[_pass])
    p_rule8 = ctrl.Rule(fuzzy2[U] & practical_marks[A], performance[_pass])
    p_rule9 = ctrl.Rule(fuzzy2[U] & practical_marks[H], performance[good])
    p_rule10 = ctrl.Rule(fuzzy2[U] & practical_marks[VH], performance[good])

    p_rule11 = ctrl.Rule(fuzzy2[A] & practical_marks[VL], performance[_pass])
    p_rule12 = ctrl.Rule(fuzzy2[A] & practical_marks[L], performance[_pass])
    p_rule13 = ctrl.Rule(fuzzy2[A] & practical_marks[A], performance[good])
    p_rule14 = ctrl.Rule(fuzzy2[A] & practical_marks[H], performance[very_good])
    p_rule15 = ctrl.Rule(fuzzy2[A] & practical_marks[VH], performance[very_good])

    p_rule16 = ctrl.Rule(fuzzy2[S] & practical_marks[VL], performance[_pass])
    p_rule17 = ctrl.Rule(fuzzy2[S] & practical_marks[L], performance[good])
    p_rule18 = ctrl.Rule(fuzzy2[S] & practical_marks[A], performance[very_good])
    p_rule19 = ctrl.Rule(fuzzy2[S] & practical_marks[H], performance[very_good])
    p_rule20 = ctrl.Rule(fuzzy2[S] & practical_marks[VH], performance[excellent])

    p_rule21 = ctrl.Rule(fuzzy2[VS] & practical_marks[VL], performance[good])
    p_rule22 = ctrl.Rule(fuzzy2[VS] & practical_marks[L], performance[very_good])
    p_rule23 = ctrl.Rule(fuzzy2[VS] & practical_marks[A], performance[very_good])
    p_rule24 = ctrl.Rule(fuzzy2[VS] & practical_marks[H], performance[excellent])
    p_rule25 = ctrl.Rule(fuzzy2[VS] & practical_marks[VH], performance[excellent])

    p_rule_list = [p_rule1, p_rule2, p_rule3, p_rule4, p_rule5, p_rule6, p_rule7, p_rule8, p_rule9,
                   p_rule10, p_rule11, p_rule12, p_rule13, p_rule14, p_rule15, p_rule16, p_rule17, p_rule18, p_rule19,
                   p_rule20, p_rule21, p_rule22, p_rule23, p_rule24, p_rule25]

    performance_ctrl = ctrl.ControlSystem(p_rule_list)

    performance_analysis = ctrl.ControlSystemSimulation(performance_ctrl)
    performance_analysis.input["Fuzzy2"] = np.array(fuzzy1_crisp)
    performance_analysis.input["Practicals"] = np.array(practical_input)
    performance_analysis.compute()

    performance_crisp = performance_analysis.output["Performance"]
    return [round(x, 2) for x in performance_crisp]


if __name__ == '__main__':
    e1 = [20, 18, 25, 31, 23, 44]
    e2 = [78, 16, 60, 39, 25, 29]
    p = [93, 13, 64, 18, 65, 92]
    print(compute_fuzzy_performance(e1, e2, p))
