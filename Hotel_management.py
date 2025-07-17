from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

class farecal:
    def __init__(self):
        self.roomrent=0
        self.service=1800
        self.name=''
        self.address=''
        self.cindate=''
        self.coutdate=''
        self.room = ''
        self.roomBooked = False
        self.total = 0

    def inputData(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Details added successfully")
            
    def roomRent(self):
        print("""
        Please select the room you want to book:
            1 => Supreme Room - Rs 3000 per night
            2 => Deluxe Room - Rs 4000 per night
            3 => Deluxe Room with Balcony - Rs 5000 per night
            4 => Deluxe Room with Balcony - Breakfast Included - Rs 6000 per night)
        """)
        room = int(input("Enter the Room:"))
        match room:
            case 1 : self.room="Supreme Room"
            case 2 : self.room = "Deluxe Room"
            case 3 : self.room = "Deluxe Room with Balcony"
            case 4 : self.room = "Deluxe Room with Balcony"
            case _ : print("Invalid choice")
        night = int(input("How many did you stayed?"))
        match room:
            case 1 : self.roomrent = night*3000
            case 2 : self.roomrent = night*4000
            case 3 : self.roomrent = night*5000
            case 4 : self.roomrent = night*5000
        self.roomBooked = True
        print("Room Booked Successfully")

    def showDetails(self):
        self.total = self.roomrent + self.service

        panel_content = f"""
        [bold cyan]NAME:[/bold cyan] {self.name}
        [bold cyan]ADDRESS:[/bold cyan] {self.address}
        [bold cyan]CHECK-IN DATE:[/bold cyan] {self.cindate}
        [bold cyan]CHECK-OUT DATE:[/bold cyan] {self.coutdate}
        """

        if self.roomBooked:
            panel_content += f"""
        [bold green]ROOM BOOKED:[/bold green] {self.room}
        [bold green]ROOM CHARGES:[/bold green] ₹{self.roomrent}
        [bold green]SERVICE CHARGES:[/bold green] ₹{self.service}
        [bold red]TOTAL BILL:[/bold red] ₹{self.total}
        """

        console.print(Panel(panel_content, title="[bold yellow]CUSTOMER DETAILS[/bold yellow]", expand=False))


def main():

    a = farecal()

    print("""
        *********************************
        *********************************
        Welcome to hotel management page
        *********************************
        *********************************
          """)
    while(1):
        menu = Table(title="Hotel Management Menu", box=None)
        menu.add_column("Option", style="bold magenta")
        menu.add_column("Description", style="cyan")

        menu.add_row("1", "Enter Customer Data")
        menu.add_row("2", "Book Room")
        menu.add_row("3", "Show Details")
        menu.add_row("4", "Exit")

        console.print(menu)

        
        opt = int(input("Enter your choice: "))
        match( opt):
            case 1 : a.inputData()
            case 2 : a.roomRent()
            case 3 : a.showDetails()
            case 4 : quit()




main()
