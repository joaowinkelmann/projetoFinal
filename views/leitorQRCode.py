import cv2
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from models.gerenciadorProdutos import GerenciadorDeProdutos

class QRCodeReader:
    def __init__(self, callback):
        self.gerenciador = GerenciadorDeProdutos()
        self.secret_key = b'mysecretkey12345'  # Replace with your own secret key
        self.callback = callback

    def start_qr_code_reading(self):
        capture = cv2.VideoCapture(0)  # Use the appropriate camera index or path

        while True:
            ret, frame = capture.read()
            cv2.imshow("QR Code Reader", frame)

            if cv2.waitKey(1) == 27:  # Exit when the Escape key is pressed
                break
        
            # Check if the window close button is pressed (for Windows)
            window_property = cv2.getWindowProperty("QR Code Reader", cv2.WND_PROP_VISIBLE)
            if window_property < 1:
                break

            detector = cv2.QRCodeDetector()
            retval, decoded_info, _, _ = detector.detectAndDecodeMulti(frame)

            if retval:
                decoded_text = decoded_info[0] if isinstance(decoded_info, tuple) else decoded_info
                print("QR Code Detected:", decoded_text)
                if self.verify_qr_code(decoded_text):
                    self.callback(decoded_text)
                    break

        capture.release()
        cv2.destroyAllWindows()

    def verify_qr_code(self, data):
        # Decode base64
        encoded_data = data.encode()
        cipher_text = base64.b64decode(encoded_data)

        # Align the data to the block boundary
        cipher_text = self.align_data_to_block_boundary(cipher_text)

        # Decrypt data
        cipher = AES.new(self.secret_key, AES.MODE_ECB)
        decrypted_data = cipher.decrypt(cipher_text)

        print(decrypted_data)

        # Remove padding if the decrypted data is not empty
        if decrypted_data:
            # Remove trailing null bytes
            unpadded_data = decrypted_data.rstrip(b'\x00')

            try:
                # Split the decoded data by '-'
                decoded_data = unpadded_data.decode().split('-')

                if len(decoded_data) == 2:
                    product_id, index = decoded_data

                    produto = self.gerenciador.buscar_produto(product_id)

                    if produto and int(index) <= produto.estoque - produto.vendido:
                        return True
            except (UnicodeDecodeError, ValueError):
                pass

        print("Invalid QR Code.")
        return False

    @staticmethod
    def align_data_to_block_boundary(data):
        # Calculate the padding size to align to block boundary
        padding_size = AES.block_size - (len(data) % AES.block_size)

        # Pad the data with the calculated size
        padded_data = data + bytes([padding_size] * padding_size)

        return padded_data
