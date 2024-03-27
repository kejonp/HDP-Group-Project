from fuzzification import output_sick_fuzzification

output_sick = output_sick_fuzzification()


class defuzzification:
    def __init__(self):
        pass

    def defuzzify(self, x):
        valRange = 1000
        delta = 5. / valRange
        points = [i * delta for i in range(valRange + 1)]
        numerator = 0.
        denominator = 0.
        for point in points:
            s1 = output_sick.outputsick_sick1(point)
            if s1 > x['outputsick_sick1']:
                s1 = x['outputsick_sick1']
            s2 = output_sick.outputsick_sick2(point)
            if s2 > x['outputsick_sick2']:
                s2 = x['outputsick_sick2']
            s3 = output_sick.outputsick_sick3(point)
            if s3 > x['outputsick_sick3']:
                s3 = x['outputsick_sick3']
            s4 = output_sick.outputsick_sick4(point)
            if s4 > x['outputsick_sick4']:
                s4 = x['outputsick_sick4']
            s_healthy = output_sick.outputsick_healthy(point)
            if s_healthy > x['outputsick_healthy']:
                s_healthy = x['outputsick_healthy']

            res = max(s1, s2, s3, s4, s_healthy)
            numerator += res * point * delta
            denominator += res * delta
        try:
            centerOfGravity = numerator / denominator
        except ZeroDivisionError:
            centerOfGravity = 0

        result = ''
        if centerOfGravity < 1.78:
          result += 'Healthy, '
        if 1.29 <= centerOfGravity <= 2.51:
            result += 'Coronary Heart Disease, '
        if 1.78 <= centerOfGravity < 3.25:
            result += 'Stroke, '
        if 1.5 <= centerOfGravity <= 4.5:
            result += 'Peripheral Arterial Disease, '
        if 3.25 <= centerOfGravity:
            result += 'Aortic Disease, '
        # return str(result) + str(centerOfGravity)
        return str(result) + str(centerOfGravity)
