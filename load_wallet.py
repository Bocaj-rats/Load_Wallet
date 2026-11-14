"""Cellphone Load Wallet: class and wallet operations."""

from decimal import Decimal, InvalidOperation


class LoadWallet:
    """Manage a subscriber's prepaid load balance."""

    SERVICE_FEE = Decimal("5.00")
    NETWORKS = ("Globe", "Smart", "DITO")

    def __init__(self, owner_name, mobile_number, starting_balance, network):
        if not owner_name.strip():
            raise ValueError("Owner name cannot be empty.")
        self._check_number(mobile_number)
        if network not in self.NETWORKS:
            raise ValueError("Please select a supported network.")

        self.owner_name = owner_name.strip()
        self.mobile_number = mobile_number
        self.network = network
        self._balance = self._check_money(starting_balance, allow_zero=True)

    @property
    def balance(self):
        """Read the balance without letting outside code change it directly."""
        return self._balance

    @staticmethod
    def _check_number(number):
        # Reminder: Philippine mobile numbers must have 11 digits and start with 09.
        if not (number.isdigit() and len(number) == 11 and number.startswith("09")):
            raise ValueError("Enter an 11-digit mobile number starting with 09.")

    @staticmethod
    def _check_money(value, allow_zero=False):
        # Reminder: Decimal prevents common floating-point issues with money.
        try:
            amount = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise ValueError("Enter a valid amount.") from None

        if not amount.is_finite() or amount < 0 or (not allow_zero and amount == 0):
            raise ValueError("Amount must be positive." if not allow_zero else "Amount cannot be negative.")
        if amount.as_tuple().exponent < -2:
            raise ValueError("Enter no more than two decimal places.")
        try:
            return amount.quantize(Decimal("0.01"))
        except InvalidOperation:
            raise ValueError("Amount is too large.") from None

    def top_up(self, amount):
        """Add prepaid load to the wallet."""
        amount = self._check_money(amount)
        self._balance += amount
        return amount

    def send_load(self, recipient_number, amount, recipient_network):
        """Send load without a fee if the recipient uses the same network."""
        self._check_number(recipient_number)
        if recipient_number == self.mobile_number:
            raise ValueError("You cannot send load to your own number.")
        if recipient_network != self.network:
            raise ValueError("Different network detected. Use Send with Fee instead.")
        amount = self._check_money(amount)
        if amount > self._balance:
            raise ValueError("Insufficient load balance.")
        self._balance -= amount
        return amount

    def send_with_fee(self, recipient_number, amount, recipient_network):
        """Send to a different network and charge the fixed service fee."""
        self._check_number(recipient_number)
        if recipient_number == self.mobile_number:
            raise ValueError("You cannot send load to your own number.")
        if recipient_network not in self.NETWORKS:
            raise ValueError("Please select a supported network.")
        if recipient_network == self.network:
            raise ValueError("Same network detected. Use Send Load instead.")
        amount = self._check_money(amount)
        total = amount + self.SERVICE_FEE
        if total > self._balance:
            raise ValueError(f"Insufficient load. You need PHP {total:.2f} including the fee.")
        self._balance -= total
        return amount, self.SERVICE_FEE, total

    def show_balance(self):
        """Return formatted wallet details for display."""
        return (
            f"Owner          : {self.owner_name}\n"
            f"Mobile Number  : {self.mobile_number}\n"
            f"Network        : {self.network}\n"
            f"Load Balance   : PHP {self._balance:.2f}"
        )
