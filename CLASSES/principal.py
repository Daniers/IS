# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI_CLASSES.principal import Ui_principal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Principal(QtGui.QMainWindow):
    """
        Clase que hace referencia a la ventana principal de la aplicación y
        todas las funciones. (Aún en desarrollo)

        Args:
            permisos (Gmail API Service Object): Servicio de autorización
                                                de acceso a la cuenta.

        Attributes:
            principal (Ui_principal): Ventana principal del entorno en Qt.
            gmail_service :Servicio de autorización de acceso a la cuenta gmail
    """
    def __init__(self, permisos):
        super(Principal, self).__init__()
        self.principal = Ui_principal()
        self.principal.setupUi(self)
        self.gmail_service = permisos
        results = self.gmail_service.users().getProfile(userId='me').execute()
        user = results.get('emailAddress',[])
        total_msg = results.get('messagesTotal',[])
        self.principal.lb_usuario.setText(user)
        self.principal.lb_total.setText(str(total_msg))