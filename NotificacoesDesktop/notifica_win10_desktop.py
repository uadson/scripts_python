from win10toast import ToastNotifier


# Start
toaster = ToastNotifier()


# Params and Notification
toaster.show_toast(
	'Notificação',
	'Python é Massa!',

	threaded=True,
	icon_path=None,
	duration=5 # 5 segundos
)