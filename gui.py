import customtkinter as ctk

class ModernDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")
        self.title("Modern Dashboard")
        self.configure(bg="#1F1F2E")

        # Navigation Bar
        self.navbar = ctk.CTkFrame(self, fg_color="#2C2C3A")
        self.navbar.pack(side="top", fill="x")

        self.nav_home = ctk.CTkButton(self.navbar, text="Home", width=100, fg_color="#2C2C3A", hover_color="#414157")
        self.nav_home.pack(side="left", padx=10, pady=10)

        self.nav_search = ctk.CTkButton(self.navbar, text="Search", width=100, fg_color="#2C2C3A", hover_color="#414157")
        self.nav_search.pack(side="left", padx=10, pady=10)

        self.nav_settings = ctk.CTkButton(self.navbar, text="Settings", width=100, fg_color="#2C2C3A", hover_color="#414157")
        self.nav_settings.pack(side="left", padx=10, pady=10)

        # Main Content Area
        self.main_frame = ctk.CTkFrame(self, fg_color="#1F1F2E")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Left Column (Login & Unlock)
        self.left_frame = ctk.CTkFrame(self.main_frame, fg_color="#2C2C3A", corner_radius=10)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.login_label = ctk.CTkLabel(self.left_frame, text="Login", font=("Helvetica", 20), text_color="white")
        self.login_label.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Email", width=200)
        self.email_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Password", show="*", width=200)
        self.password_entry.pack(pady=5)

        self.forgot_button = ctk.CTkButton(self.left_frame, text="Forgot Password?", fg_color="#2C2C3A", hover_color="#414157", text_color="white")
        self.forgot_button.pack(pady=10)

        self.signup_button = ctk.CTkButton(self.left_frame, text="Sign Up", fg_color="#3D5AF1", hover_color="#2E47CC")
        self.signup_button.pack(pady=10)

        # Unlock Button
        self.unlock_button = ctk.CTkButton(self.left_frame, text="Swipe to unlock", fg_color="#3D5AF1", hover_color="#2E47CC")
        self.unlock_button.pack(pady=20)

        # Center Column (Graph & Analytics)
        self.center_frame = ctk.CTkFrame(self.main_frame, fg_color="#2C2C3A", corner_radius=10)
        self.center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.graph_label = ctk.CTkLabel(self.center_frame, text="Today\n$62,970", font=("Helvetica", 24), text_color="white")
        self.graph_label.pack(pady=20)

        self.transaction_button = ctk.CTkButton(self.center_frame, text="Transaction", fg_color="#3D5AF1", hover_color="#2E47CC")
        self.transaction_button.pack(pady=10)

        # Right Column (Settings & Analytics)
        self.right_frame = ctk.CTkFrame(self.main_frame, fg_color="#2C2C3A", corner_radius=10)
        self.right_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.settings_label = ctk.CTkLabel(self.right_frame, text="Settings", font=("Helvetica", 20), text_color="white")
        self.settings_label.pack(pady=10)

        self.food_label = ctk.CTkLabel(self.right_frame, text="Food", font=("Helvetica", 16), text_color="white")
        self.food_label.pack(anchor="w", padx=20)
        self.food_bar = ctk.CTkProgressBar(self.right_frame, progress_color="#3D5AF1")
        self.food_bar.set(0.5)
        self.food_bar.pack(fill="x", padx=20, pady=5)

        self.savings_label = ctk.CTkLabel(self.right_frame, text="Savings", font=("Helvetica", 16), text_color="white")
        self.savings_label.pack(anchor="w", padx=20)
        self.savings_bar = ctk.CTkProgressBar(self.right_frame, progress_color="#F1A93D")
        self.savings_bar.set(0.7)
        self.savings_bar.pack(fill="x", padx=20, pady=5)

        self.rent_label = ctk.CTkLabel(self.right_frame, text="Rent", font=("Helvetica", 16), text_color="white")
        self.rent_label.pack(anchor="w", padx=20)
        self.rent_bar = ctk.CTkProgressBar(self.right_frame, progress_color="#47F13D")
        self.rent_bar.set(0.4)
        self.rent_bar.pack(fill="x", padx=20, pady=5)

        self.analytics_label = ctk.CTkLabel(self.right_frame, text="6k", font=("Helvetica", 20), text_color="white")
        self.analytics_label.pack(pady=10)
app.mainloop()
# if __name__ == "__gui__":
#     app = ModernDashboard()
#     app.mainloop()
