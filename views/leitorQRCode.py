import cv2
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from models.gerenciadorProdutos import GerenciadorDeProdutos
from models.salvaArquivo import QRLog
import time

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
                if self.verify_qr_code(decoded_text):
                    self.callback(decoded_text)
                    break

            time.sleep(0.1)  # Introduce a delay of 100 milliseconds (0.1 seconds)

        capture.release()
        cv2.destroyAllWindows()

    def verify_qr_code(self, data):
        qrcodes = QRLog.carregar_qr_codes()  # Load QR codes from the file

        for qrcode in qrcodes:
            if data == qrcode[0]:
                if not qrcode[1]:
                    print("OK!")
                    # Mark the QR code as used and save the updated QR codes to the file
                    qrcode[1] = True
                    QRLog.salvar_qr_code(qrcodes)
                    return True

        return False

    @staticmethod
    def align_data_to_block_boundary(data):
        # Calculate the padding size to align to block boundary
        padding_size = AES.block_size - (len(data) % AES.block_size)

        # Pad the data with the calculated size
        padded_data = data + bytes([padding_size] * padding_size)

        return padded_data
