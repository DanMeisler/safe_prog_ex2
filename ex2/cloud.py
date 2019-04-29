
# you don't have to use the packages below, it is only a suggestion. 
# do not use any other python module unless it is explicitly permitted by the instructor.
from Crypto import Random
from Crypto.Util import Counter
import Crypto.Cipher.AES as AES


class Cloud:
	"""
	the cloud stores your content encrypted.
	you can add variables and methods to this class as you want.
	you don't have to use the following properties, it is just one direction for implementation.
	"""

	def __init__(self, filename):
		"""
		Encrypt the content of 'filename' and store its ciphertext at self.ciphertext
		The encryption to use here is AES-CTR.
		"""
		self._filename = filename
		self._key = Random.get_random_bytes(32)
		self._nonce = Random.get_random_bytes(8)
		self._cipher_text = None
		self._construct_cipher_text()

	def Read(self, position=0):
		"""
		Returns one byte at 'position' from current self.ciphertext.
		position=0 returns the first byte of the ciphertext.
		"""
		return self._cipher_text[position]

	def Write(self, position=0, newbyte='\x33'):
		"""
		Replace the byte in 'position' from self.ciphertext with the encryption of 'newbyte'.
		Remember that you should encrypt 'newbyte' under the appropriate key (it depends on the position).
		Return the previous byte from self.ciphertext (before the re-write).
		"""
		before_rewrite = self.Read(position)
		to_encrypt = "\x00" * position + newbyte
		crypto = AES.new(self._key, AES.MODE_CTR, counter=Counter.new(64, self._nonce))
		self._cipher_text[position] = crypto.encrypt(to_encrypt)[position]
		return before_rewrite

	def _construct_cipher_text(self):
		plain_text = self._read_plain_text()
		crypto = AES.new(self._key, AES.MODE_CTR, counter=Counter.new(64, self._nonce))
		self._cipher_text = bytearray(crypto.encrypt(plain_text))

	def _read_plain_text(self):
		with open(self._filename) as f:
			return f.read()

