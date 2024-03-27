#     Copyright 2024 Group 2 AI Course MIE212401 Final Project

#     Licensed by Jules
#     you may not use this file for public use except in compliance with the license.
#     you may obtain a copy of the license at

#     julianrafi@gmail.com

#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

#     Author: Julian Rafi

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
        if 1.29 <= centerOfGravity <= 2.53:
            result += 'Coronary Heart Disease, '
        if 1.98 <= centerOfGravity < 3.21:
            result += 'Stroke, '
        if 1.71 <= centerOfGravity <= 2.5:
            result += 'Peripheral Arterial Disease, '
        if 3.25 <= centerOfGravity:
            result += 'Aortic Disease, '
        return str(result) + str(centerOfGravity)
        # return str(result) 
