"""

"""


class SkillImpactEffect(object):
    """
        技能影响效果
    """

    def impact(self):
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        造成伤害效果
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


class LowerDefenseEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%d防御力，持续%d秒" % (self.value, self.time))


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕效果
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕%d秒" % self.time)


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, name):
        self.name = name
        # 加载配置文件{技能名称:[效果1,效果2]}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_objects = self.__create_effect_object()

    def __load_config_file(self):
        return {
            "降龙十八掌": ["DamageEffect(200)", "LowerDefenseEffect(-10, 5)", "DizzinessEffect(3)"],
            "六脉神剑": ["DamageEffect(150)", "LowerDefenseEffect(-8, 3)"]
        }

    def __create_effect_object(self):
        # 根据name创建相应的技能对象
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for effect in list_effect_name:
            effect_object = eval(effect)
            list_effect_object.append(effect_object)
        return list_effect_object

    # 生成技能(执行效果)
    def generate_skill(self):
        print(self.name, "技能释放啦")
        for item in self.__effect_objects:
            item.impact()


xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()
lmsj = SkillDeployer("六脉神剑")
lmsj.generate_skill()
