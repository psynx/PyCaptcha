from multicolorcaptcha.multicolorcaptcha import CaptchaGenerator
import json, random
class gencaptcha:
  def math():
    filename = str(random.randint(0,9999))
    CAPCTHA_SIZE_NUM = 1
    generator = CaptchaGenerator(CAPCTHA_SIZE_NUM)
    math_captcha = generator.gen_math_captcha_image(difficult_level=0,margin=False,multicolor=True)
    math_image = math_captcha["image"]
    math_equation_string = math_captcha["equation_str"]
    math_equation_result = math_captcha["equation_result"]
#    print(str(math_equation_result))
    math_image.save(f"img/{filename}.png", "png")
    out = {'answer':str(math_equation_result),'image':f'{filename}'}
    return json.dumps(out)
gencaptcha.math()
