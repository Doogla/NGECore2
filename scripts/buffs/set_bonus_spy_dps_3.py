import sys

def setup(core, actor, buff):
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_action_line_sp_dm', 20)
	core.skillModService.addSkillMod(actor, 'fast_attack_line_sp_dm', 15)
	core.skillModService.addSkillMod(actor, 'expertise_freeshot_sp_dm', 20)
	core.skillModService.addSkillMod(actor, 'expertise_cooldown_line_sp_dm', 20)
	core.skillModService.addSkillMod(actor, 'expertise_action_line_sp_dot', 25)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_action_line_sp_dm', 20)
	core.skillModService.deductSkillMod(actor, 'fast_attack_line_sp_dm', 15)
	core.skillModService.deductSkillMod(actor, 'expertise_freeshot_sp_dm', 20)
	core.skillModService.deductSkillMod(actor, 'expertise_cooldown_line_sp_dm', 20)
	core.skillModService.deductSkillMod(actor, 'expertise_action_line_sp_dot', 25)
	return