# Python equivalent of the C# ConsoleUI Program

# Import statements (equivalent to C# using statements)
from Business.Concrete.CategoryManager import CategoryManager
from Business.Concrete.NeglectManager import NeglectManager
from Core.DataAccess.IEntitiyRepository import EfCategoryDal


class Program:
    @staticmethod
    def main():
        """Main entry point of the program"""
        # Uncomment the methods you want to test
        # Program.product_test()
        # Program.category_test()
        pass
    
    @staticmethod
    def category_test():
        """Test method for category operations"""
        category_manager = CategoryManager(EfCategoryDal())
        result = category_manager.get_all()
        
        if result.success:
            for category in result.data:
                print(category.category_name)
        else:
            print(result.message)
    

# Entry point for Python script
if __name__ == "__main__":
    Program.main()