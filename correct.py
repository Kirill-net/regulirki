import re

class Correct:
  def __init__(self, contacts_list):
    self.contacts_list = contacts_list
    self.subst1 = r'+7(\2)\3-\4-\5'
    self.subst2 = r'+7(\2)\3-\4-\5 доб.\6'
    self.pattern2 = r"(\+7|8)\W\(?(\d{3})\W\s?(\d{3})\W(\d{2})\W?(\d{2})\W?\(?доб.\W?(\d{4})\W?"
    self.pattern1 = r"(\+7|8) ?\W?(\d{3})\W? ?(\d{3})\W?(\d{2})\W?(\d{2})"

  def correct_name(self):
    for indx, fls in enumerate(self.contacts_list):
      fls = " ".join(fls[:3])
      name = fls.split()
      if len(name) != 3:
        name += ['']
      self.contacts_list[indx][:3] = name

  def correct_phone(self):
    for indx, fls in enumerate(self.contacts_list[1:]):
      if 'доб' in fls[5]:
        self.contacts_list[indx+1][5] = re.sub(self.pattern2, self.subst2, fls[5])
      elif 'доб' not in fls[5] and len(fls[5]) > 0:
        self.contacts_list[indx+1][5] = re.sub(self.pattern1, self.subst1, fls[5])

  def united(self):
    for ind1, line1 in enumerate(self.contacts_list):
      for ind2, line2 in enumerate(self.contacts_list):
        if line1 != line2 and line1[0] == line2[0] and line1[1] == line2[1]:
          for ind3, el in enumerate(line1):
            if el == "":
              self.contacts_list[ind1][ind3] = line2[ind3]
          self.contacts_list.pop(ind2)
