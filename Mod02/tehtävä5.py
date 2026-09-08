import math

class Lieviskä:
	"""Represents a weight expressed in leiviskät, naulat and luodit."""

	GRAMS_PER_LEIVISKÄ = 8_500
	GRAMS_PER_NAULA = 425
	GRAMS_PER_LUOTI = 13.3

	def __init__(self, leiviskät=0, naulat=0, luodit=0):
		self.leiviskät = leiviskät
		self.naulat = naulat
		self.luodit = luodit

	def grams(self):
		"""Return the total weight in grams."""
		return (
			self.leiviskät * self.GRAMS_PER_LEIVISKÄ
			+ self.naulat * self.GRAMS_PER_NAULA
			+ self.luodit * self.GRAMS_PER_LUOTI
		)

	def kilograms(self):
		"""Return the total weight in kilograms."""
		return self.grams() / 1000
	

	def __str__(self):
		return f"{self.grams():.1f} g ({self.kilograms():.3f} kg)"
	


leiviskät = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
paino = Lieviskä(leiviskät, naulat, luodit)
print(f"Paino: {paino}")




