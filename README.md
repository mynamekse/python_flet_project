# Flet Python Project - MVVM Pattern

A modern Flet application demonstrating form handling with **MVVM (Model-View-ViewModel)** architecture pattern, enabling clean separation of business logic from UI.

## 🌟 Features

- 🎨 Modern UI with custom components
- 📝 Form validation with real-time feedback
- 🔄 Multiple views with smooth navigation
- 🏗️ **MVVM Architecture** - Separates business logic from UI
- 🧪 **Testable** - Business logic can be tested independently
- 🌓 Dark mode support
- 🎯 Clean, maintainable code structure

## 📋 Default Credentials

For testing the application, use these default credentials:

**Email:** `demo@example.com`  
**Password:** `password123`

> **Note:** This is a demo application. Any valid email format with a password of at least 6 characters will work.

## 🏗️ Project Structure (MVVM Pattern)

```
python_flet_project/
├── src/
│   ├── main.py                 # Application entry point
│   ├── models/                 # Data models (M in MVVM)
│   │   ├── __init__.py
│   │   ├── user_model.py
│   │   └── settings_model.py
│   ├── viewmodels/            # Business logic (VM in MVVM)
│   │   ├── __init__.py
│   │   ├── base_viewmodel.py
│   │   ├── login_viewmodel.py
│   │   ├── home_viewmodel.py
│   │   └── settings_viewmodel.py
│   ├── views/                 # UI layer (V in MVVM)
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   ├── home_view.py
│   │   └── settings_view.py
│   ├── components/            # Reusable UI components
│   │   ├── __init__.py
│   │   ├── custom_button.py
│   │   ├── custom_card.py
│   │   └── custom_input.py
│   ├── services/              # External services
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── storage_service.py
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       ├── validators.py
│       └── theme.py
├── tests/                     # Unit tests
├── assets/                    # Static assets
├── pyproject.toml            # Project configuration
└── README.md
```

## 🚀 Installation

### Prerequisites

- **Python 3.10 or higher**
- **UV package manager** (recommended) or pip

### Step 1: Install UV (if not already installed)

```bash
pip install uv
```

### Step 2: Clone or navigate to the project directory

```bash
cd f:\python_projects\python_flet_project
```

### Step 3: Install dependencies

**Option A: Using UV (Recommended)**
```bash
uv sync
```

**Option B: Using UV with virtual environment**
```bash
uv venv
uv pip install -e .
```

**Option C: Using pip**
```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

### Method 1: Using UV (Recommended)

```bash
uv run python src/main.py
```

### Method 2: Using Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
python src/main.py
```

**Linux/Mac:**
```bash
source .venv/bin/activate
python src/main.py
```

### Method 3: Direct Python

```bash
python src/main.py
```

## 🎮 How to Use

1. **Login Screen**
   - Enter email: `demo@example.com`
   - Enter password: `password123`
   - Click "Login" button
   - Or use any valid email format with 6+ character password

2. **Home Screen**
   - View welcome message
   - Navigate to Settings
   - Logout to return to login

3. **Settings Screen**
   - Update display name
   - Add bio information
   - Toggle dark mode
   - Save settings

## 🏛️ MVVM Architecture Benefits

### Why MVVM?

- ✅ **Logic-First Development**: Develop and test business logic without UI
- ✅ **Testability**: Unit test ViewModels independently
- ✅ **Separation of Concerns**: Clear boundaries between layers
- ✅ **Maintainability**: Easy to modify UI or logic separately
- ✅ **Reusability**: ViewModels can be reused across different views

### Example Workflow

```python
# 1. Develop ViewModel (Pure Python - No UI needed!)
vm = LoginViewModel()
vm.email = "test@example.com"
vm.password = "password123"
result = vm.login()  # Test logic without UI

# 2. Create View (Later)
view = LoginView(page, viewmodel=vm)  # Bind to existing logic
```

## 🧪 Testing

### Test ViewModels (No UI Required)

```bash
# Run unit tests for business logic
uv run python -m pytest tests/

# Test specific ViewModel
uv run python -m pytest tests/test_login_viewmodel.py
```

### Manual Testing

1. Run the application
2. Test login with valid/invalid credentials
3. Test form validation (empty fields, invalid email, short password)
4. Test navigation between views
5. Test settings save functionality
6. Test dark mode toggle

## 🛠️ Development

### Adding a New Feature

1. **Create Model** (if needed)
   ```python
   # src/models/new_model.py
   @dataclass
   class NewModel:
       field: str
   ```

2. **Create ViewModel** (Business Logic)
   ```python
   # src/viewmodels/new_viewmodel.py
   class NewViewModel(BaseViewModel):
       def __init__(self):
           super().__init__()
           self.data = ""
       
       def process_data(self):
           # Business logic here
           self.notify_listeners()
   ```

3. **Create View** (UI)
   ```python
   # src/views/new_view.py
   class NewView(ft.View):
       def __init__(self, page, viewmodel):
           self.viewmodel = viewmodel
           self.viewmodel.add_listener(self.update_ui)
   ```

4. **Test ViewModel First** (Before UI)
   ```python
   # tests/test_new_viewmodel.py
   def test_process_data():
       vm = NewViewModel()
       vm.data = "test"
       vm.process_data()
       assert vm.data == "processed"
   ```

## 📦 Dependencies

- **flet** >= 0.24.1 - Modern UI framework for Python

## 🤝 Contributing

1. Follow MVVM pattern
2. Keep ViewModels pure (no Flet dependencies)
3. Write unit tests for ViewModels
4. Use custom components for consistent UI

## 📝 License

MIT

## 🔗 Resources

- [Flet Documentation](https://flet.dev)
- [MVVM Pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
- [UV Package Manager](https://github.com/astral-sh/uv)
