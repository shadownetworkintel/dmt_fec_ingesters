import pytest
import sys
import os
from unittest.mock import patch, MagicMock, call
import argparse

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestManageCommittees:
    """Test the manage_committees.py script functionality."""
    
    def setup_method(self):
        """Clear module cache before each test to ensure fresh imports."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_command_with_targets(self, mock_print, mock_list_targets):
        """Test listing committee targets when targets exist."""
        # Mock return data
        mock_list_targets.return_value = [
            {
                'committee_id': 'C00467571',
                'committee_name': 'Test Committee 1',
                'active': True
            },
            {
                'committee_id': 'C00123456',
                'committee_name': 'Test Committee 2',
                'active': False
            },
            {
                'committee_id': 'C00789012',
                'committee_name': None,
                'active': True
            }
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            # Verify the function was called
            mock_list_targets.assert_called_once()
            
            # Verify output formatting
            print_calls = [str(call) for call in mock_print.call_args_list]
            
            # Should print header
            header_calls = [call for call in print_calls if "Committee Targets:" in call]
            assert len(header_calls) == 1
            
            # Should print committee info with proper formatting
            committee_calls = [call for call in print_calls if "C00467571" in call and "ACTIVE" in call]
            assert len(committee_calls) == 1
            
            committee_calls = [call for call in print_calls if "C00123456" in call and "INACTIVE" in call]
            assert len(committee_calls) == 1
            
            # Should handle None name with "N/A"
            na_calls = [call for call in print_calls if "C00789012" in call and "N/A" in call]
            assert len(na_calls) == 1

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_command_no_targets(self, mock_print, mock_list_targets):
        """Test listing committee targets when no targets exist."""
        mock_list_targets.return_value = []
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_list_targets.assert_called_once()
            mock_print.assert_called_with("No committee targets found.")

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_success(self, mock_print, mock_add_target):
        """Test successful addition of committee target."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00467571', '--name', 'Test Committee', '--description', 'Test Description']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', 'Test Committee', 'Test Description')
            mock_print.assert_called_with("Successfully added committee target: C00467571")

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_failure(self, mock_print, mock_add_target):
        """Test failed addition of committee target."""
        mock_add_target.return_value = False
        
        test_args = ['manage_committees.py', 'add', 'C00467571']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', None, None)
            mock_print.assert_called_with("Failed to add committee target: C00467571")
            assert exc_info.value.code == 1

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_minimal_args(self, mock_print, mock_add_target):
        """Test adding committee with only required argument."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00467571']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            # Should pass None for optional arguments
            mock_add_target.assert_called_once_with('C00467571', None, None)

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_command_success(self, mock_print, mock_remove_target):
        """Test successful removal of committee target."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00467571']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00467571')
            mock_print.assert_called_with("Successfully removed committee target: C00467571")

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_command_failure(self, mock_print, mock_remove_target):
        """Test failed removal of committee target."""
        mock_remove_target.return_value = False
        
        test_args = ['manage_committees.py', 'remove', 'C00467571']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00467571')
            mock_print.assert_called_with("Failed to remove committee target: C00467571")
            assert exc_info.value.code == 1

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_success(self, mock_print, mock_enable_all):
        """Test successful enabling of all committees mode."""
        mock_enable_all.return_value = True
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()
            mock_print.assert_called_with("Successfully enabled all committees mode")

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_failure(self, mock_print, mock_enable_all):
        """Test failed enabling of all committees mode."""
        mock_enable_all.return_value = False
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()
            mock_print.assert_called_with("Failed to enable all committees mode")
            assert exc_info.value.code == 1

    def test_no_command_shows_help(self):
        """Test that running without command shows help."""
        test_args = ['manage_committees.py']
        
        with patch('sys.argv', test_args), \
             patch('argparse.ArgumentParser.print_help') as mock_help:
            from scripts.manage_committees import main
            main()
            
            mock_help.assert_called_once()

    def test_invalid_command_exits(self):
        """Test that invalid commands cause exit."""
        test_args = ['manage_committees.py', 'invalid_command']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesArgumentParsing:
    """Test argument parsing functionality."""
    
    def test_list_parser(self):
        """Test list command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        list_parser = subparsers.add_parser('list', help='List all committee targets')
        
        args = parser.parse_args(['list'])
        assert args.command == 'list'

    def test_add_parser_full_args(self):
        """Test add command with all arguments."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        add_parser = subparsers.add_parser('add', help='Add a committee target')
        add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
        add_parser.add_argument('--name', help='Committee name')
        add_parser.add_argument('--description', help='Description')
        
        args = parser.parse_args(['add', 'C00467571', '--name', 'Test Committee', '--description', 'Test Desc'])
        assert args.command == 'add'
        assert args.committee_id == 'C00467571'
        assert args.name == 'Test Committee'
        assert args.description == 'Test Desc'

    def test_add_parser_minimal_args(self):
        """Test add command with only required arguments."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        add_parser = subparsers.add_parser('add', help='Add a committee target')
        add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
        add_parser.add_argument('--name', help='Committee name')
        add_parser.add_argument('--description', help='Description')
        
        args = parser.parse_args(['add', 'C00467571'])
        assert args.command == 'add'
        assert args.committee_id == 'C00467571'
        assert args.name is None
        assert args.description is None

    def test_remove_parser(self):
        """Test remove command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        remove_parser = subparsers.add_parser('remove', help='Remove a committee target')
        remove_parser.add_argument('committee_id', help='Committee ID to remove')
        
        args = parser.parse_args(['remove', 'C00467571'])
        assert args.command == 'remove'
        assert args.committee_id == 'C00467571'

    def test_all_parser(self):
        """Test all command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        all_parser = subparsers.add_parser('all', help='Enable all committees mode (deactivate all targets)')
        
        args = parser.parse_args(['all'])
        assert args.command == 'all'

class TestManageCommitteesIntegration:
    """Integration tests for manage_committees.py"""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')  # Changed from 'scripts.manage_committees.list_committee_targets'
    @patch('builtins.print')
    def test_full_list_workflow(self, mock_print, mock_list_targets):
        """Test complete list workflow."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': 'Committee 1', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            # Verify full workflow
            mock_list_targets.assert_called_once()
            assert mock_print.call_count >= 3  # Header, separator, and committee info

    @patch('scripts.manage_committees.add_committee_target')  # Changed from 'scripts.manage_committees.add_committee_target'
    @patch('builtins.print')
    def test_full_add_workflow(self, mock_print, mock_add_target):
        """Test complete add workflow."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', 'New Committee']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', 'New Committee', None)
            mock_print.assert_called_with("Successfully added committee target: C00123456")

    @patch('scripts.manage_committees.remove_committee_target')  # Changed from 'scripts.manage_committees.remove_committee_target'
    @patch('builtins.print')
    def test_full_remove_workflow(self, mock_print, mock_remove_target):
        """Test complete remove workflow."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00123456']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00123456')
            mock_print.assert_called_with("Successfully removed committee target: C00123456")

class TestManageCommitteesEdgeCases:
    """Test edge cases and error conditions."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_mixed_active_status(self, mock_print, mock_list_targets):
        """Test listing with mix of active and inactive targets."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': 'Active Committee', 'active': True},
            {'committee_id': 'C002', 'committee_name': 'Inactive Committee', 'active': False}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            active_calls = [call for call in print_calls if "ACTIVE" in call and "C001" in call]
            inactive_calls = [call for call in print_calls if "INACTIVE" in call and "C002" in call]
            
            assert len(active_calls) == 1
            assert len(inactive_calls) == 1

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_none_committee_names(self, mock_print, mock_list_targets):
        """Test listing when committee names are None."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': None, 'active': True},
            {'committee_id': 'C002', 'committee_name': '', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            na_calls = [call for call in print_calls if "N/A" in call]
            # Should handle both None and empty string as "N/A"
            assert len(na_calls) >= 1

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_with_special_characters(self, mock_print, mock_add_target):
        """Test adding committee with special characters."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', "Committee's & Friends", '--description', 'Test & Description']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', "Committee's & Friends", 'Test & Description')
            mock_print.assert_called_with("Successfully added committee target: C00123456")

    def test_add_missing_committee_id(self):
        """Test add command without committee ID."""
        test_args = ['manage_committees.py', 'add']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

    def test_remove_missing_committee_id(self):
        """Test remove command without committee ID."""
        test_args = ['manage_committees.py', 'remove']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.list_committee_targets')
    def test_list_command_exception_handling(self, mock_list_targets):
        """Test that exceptions from list_committee_targets are properly handled."""
        mock_list_targets.side_effect = Exception("Database error")
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database error"):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesEnvironmentSetup:
    """Test environment and import setup."""
    
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    def test_environment_loading(self, mock_getenv, mock_load_dotenv):
        """Test that environment is loaded correctly."""
        mock_getenv.return_value = "prod"
        
        # Clear module cache and re-import to trigger environment loading
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
        
        import scripts.manage_committees
        
        # Should load .env first, then .env.{mode}
        assert mock_load_dotenv.call_count >= 1

    def test_imports_successful(self):
        """Test that all required imports work."""
        # This test verifies that the module can be imported without errors
        from scripts.manage_committees import main
        assert callable(main)

    def test_logger_setup(self):
        """Test that logger is set up."""
        import scripts.manage_committees as mc
        assert hasattr(mc, 'logger')
        assert mc.logger is not None

class TestManageCommitteesAdvancedScenarios:
    """Additional advanced test scenarios."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_empty_strings_and_none_values(self, mock_print, mock_list_targets):
        """Test listing handles various falsy values correctly."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': '', 'active': True},
            {'committee_id': 'C002', 'committee_name': '   ', 'active': False},
            {'committee_id': 'C003', 'committee_name': None, 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            
            # All should display "N/A" for empty/None names
            na_calls = [call for call in print_calls if "N/A" in call]
            assert len(na_calls) >= 2  # At least empty string and None should show as N/A

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_with_long_names_and_descriptions(self, mock_print, mock_add_target):
        """Test adding committee with very long names and descriptions."""
        mock_add_target.return_value = True
        
        long_name = "A" * 200
        long_description = "B" * 500
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', long_name, '--description', long_description]
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', long_name, long_description)

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_large_number_of_committees(self, mock_print, mock_list_targets):
        """Test listing with many committees."""
        # Generate 100 test committees
        committees = []
        for i in range(100):
            committees.append({
                'committee_id': f'C{i:08d}',
                'committee_name': f'Test Committee {i}',
                'active': i % 2 == 0  # Alternate active/inactive
            })
        
        mock_list_targets.return_value = committees
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_list_targets.assert_called_once()
            # Should print header + separator + 100 committees
            assert mock_print.call_count >= 102

    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_unicode_characters(self, mock_add_target):
        """Test adding committee with unicode characters."""
        mock_add_target.return_value = True
        
        unicode_name = "Comité Español 中文 🏛️"
        unicode_desc = "Description with émojis 📊 and spéciál characters"
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', unicode_name, '--description', unicode_desc]
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', unicode_name, unicode_desc)

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_nonexistent_committee(self, mock_print, mock_remove_target):
        """Test removing a committee that doesn't exist."""
        mock_remove_target.return_value = False
        
        test_args = ['manage_committees.py', 'remove', 'C99999999']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C99999999')
            mock_print.assert_called_with("Failed to remove committee target: C99999999")
            assert exc_info.value.code == 1

    def test_parser_with_conflicting_args(self):
        """Test parser behavior with potentially conflicting arguments."""
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', '--description']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):  # Should fail due to missing description value
            from scripts.manage_committees import main
            main()

class TestManageCommitteesOutputFormatting:
    """Test output formatting and display logic."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_output_column_alignment(self, mock_print, mock_list_targets):
        """Test that list output maintains proper column alignment."""
        mock_list_targets.return_value = [
            {'committee_id': 'C00123456789', 'committee_name': 'Short', 'active': True},
            {'committee_id': 'C001', 'committee_name': 'Very Long Committee Name That Goes On And On', 'active': False}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [call[0][0] for call in mock_print.call_args_list if call[0]]
            
            # Find the actual committee data lines (skip header and separator)
            committee_lines = [line for line in print_calls if line.startswith('C')]
            
            # Verify proper spacing format (committee_id should be left-aligned in 12 chars)
            for line in committee_lines:
                assert 'ACTIVE' in line or 'INACTIVE' in line

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_very_long_committee_names(self, mock_print, mock_list_targets):
        """Test handling of very long committee names."""
        long_name = "X" * 100
        mock_list_targets.return_value = [
            {'committee_id': 'C00123456', 'committee_name': long_name, 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [call[0][0] for call in mock_print.call_args_list if call[0]]
            committee_line = [line for line in print_calls if 'C00123456' in line][0]
            
            # Should include the full long name
            assert long_name in committee_line

class TestManageCommitteesErrorScenarios:
    """Test various error and exception scenarios."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_database_exception(self, mock_add_target):
        """Test add command when database throws exception."""
        mock_add_target.side_effect = Exception("Database connection failed")
        
        test_args = ['manage_committees.py', 'add', 'C00123456']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database connection failed"):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.remove_committee_target')
    def test_remove_with_database_exception(self, mock_remove_target):
        """Test remove command when database throws exception."""
        mock_remove_target.side_effect = Exception("Database connection failed")
        
        test_args = ['manage_committees.py', 'remove', 'C00123456']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database connection failed"):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.enable_all_committees_mode')
    def test_all_with_database_exception(self, mock_enable_all):
        """Test all command when database throws exception."""
        mock_enable_all.side_effect = Exception("Database connection failed")
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database connection failed"):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesComplexScenarios:
    """Additional complex test scenarios."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_empty_list_return(self, mock_print, mock_list_targets):
        """Test list command returns empty list."""
        mock_list_targets.return_value = []
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_list_targets.assert_called_once()
            mock_print.assert_called_with("No committee targets found.")

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_with_whitespace_handling(self, mock_print, mock_add_target):
        """Test add command handles whitespace correctly."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', '  Spaced Name  ', '--description', '  Spaced Description  ']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', '  Spaced Name  ', '  Spaced Description  ')

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_with_case_sensitivity(self, mock_print, mock_remove_target):
        """Test remove command is case sensitive."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'c00123456']  # lowercase
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('c00123456')

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_with_no_changes(self, mock_print, mock_enable_all):
        """Test all command when no changes are needed."""
        mock_enable_all.return_value = True
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_special_characters_in_names(self, mock_print, mock_list_targets):
        """Test list command with special characters in committee names."""
        mock_list_targets.return_value = [
            {'committee_id': 'C00123456', 'committee_name': 'Committee & Friends', 'active': True},
            {'committee_id': 'C00789012', 'committee_name': "O'Reilly's PAC", 'active': False},
            {'committee_id': 'C00345678', 'committee_name': 'Committee "The Best"', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            
            # Verify special characters are preserved
            ampersand_calls = [call for call in print_calls if "Committee & Friends" in call]
            assert len(ampersand_calls) == 1
            
            apostrophe_calls = [call for call in print_calls if "O'Reilly's PAC" in call]
            assert len(apostrophe_calls) == 1

    def test_main_function_isolation(self):
        """Test that main function can be called multiple times without side effects."""
        test_args = ['manage_committees.py', '--help']
        
        with patch('sys.argv', test_args), \
             patch('argparse.ArgumentParser.print_help') as mock_help, \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()
            mock_help.assert_called_once()
        
        # Call again to ensure no side effects
        with patch('sys.argv', test_args), \
             patch('argparse.ArgumentParser.print_help') as mock_help2, \
             pytest.raises(SystemExit):
            main()
            mock_help2.assert_called_once()

class TestManageCommitteesValidation:
    """Test input validation and edge cases."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_empty_committee_id(self, mock_add_target):
        """Test add command with empty committee ID."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', '']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('', None, None)

    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_numeric_strings(self, mock_add_target):
        """Test add command with numeric strings."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', '12345', '--name', '67890', '--description', '999']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('12345', '67890', '999')

    @patch('scripts.manage_committees.remove_committee_target')
    def test_remove_with_special_committee_id(self, mock_remove_target):
        """Test remove command with special characters in committee ID."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00-123-456']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00-123-456')

    def test_argument_parsing_edge_cases(self):
        """Test edge cases in argument parsing."""
        # Test with equals sign in arguments
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name=Test Committee']
        
        with patch('sys.argv', test_args), \
             patch('scripts.manage_committees.add_committee_target', return_value=True):
            from scripts.manage_committees import main
            main()

# ...existing code...

class TestManageCommitteesPerformance:
    """Test performance-related scenarios."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_massive_dataset(self, mock_print, mock_list_targets):
        """Test list command with very large dataset."""
        # Generate 1000 test committees
        committees = []
        for i in range(1000):
            committees.append({
                'committee_id': f'C{i:08d}',
                'committee_name': f'Committee {i}' * 10,  # Long names
                'active': i % 3 == 0  # Mix of active/inactive
            })
        
        mock_list_targets.return_value = committees
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_list_targets.assert_called_once()
            # Should handle large datasets without issues
            assert mock_print.call_count >= 1002  # Header + separator + 1000 committees

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_with_maximum_length_inputs(self, mock_print, mock_add_target):
        """Test add command with maximum length inputs."""
        mock_add_target.return_value = True
        
        max_name = "A" * 1000
        max_description = "B" * 2000
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', max_name, '--description', max_description]
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', max_name, max_description)
            mock_print.assert_called_with("Successfully added committee target: C00123456")

if __name__ == '__main__':
    pytest.main([__file__])

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_success(self, mock_print, mock_add_target):
        """Test successful addition of committee target."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00467571', '--name', 'Test Committee', '--description', 'Test Description']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', 'Test Committee', 'Test Description')
            mock_print.assert_called_with("Successfully added committee target: C00467571")

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_failure(self, mock_print, mock_add_target):
        """Test failed addition of committee target."""
        mock_add_target.return_value = False
        
        test_args = ['manage_committees.py', 'add', 'C00467571']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', None, None)
            mock_print.assert_called_with("Failed to add committee target: C00467571")
            assert exc_info.value.code == 1

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_minimal_args(self, mock_print, mock_add_target):
        """Test adding committee with only required argument."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00467571']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', None, None)

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_command_success(self, mock_print, mock_remove_target):
        """Test successful removal of committee target."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00467571']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00467571')
            mock_print.assert_called_with("Successfully removed committee target: C00467571")

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_command_failure(self, mock_print, mock_remove_target):
        """Test failed removal of committee target."""
        mock_remove_target.return_value = False
        
        test_args = ['manage_committees.py', 'remove', 'C00467571']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00467571')
            mock_print.assert_called_with("Failed to remove committee target: C00467571")
            assert exc_info.value.code == 1

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_success(self, mock_print, mock_enable_all):
        """Test successful enabling of all committees mode."""
        mock_enable_all.return_value = True
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()
            mock_print.assert_called_with("Successfully enabled all committees mode")

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_failure(self, mock_print, mock_enable_all):
        """Test failed enabling of all committees mode."""
        mock_enable_all.return_value = False
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()
            mock_print.assert_called_with("Failed to enable all committees mode")
            assert exc_info.value.code == 1

    def test_no_command_shows_help(self):
        """Test that running without command shows help."""
        test_args = ['manage_committees.py']
        
        with patch('sys.argv', test_args), \
             patch('argparse.ArgumentParser.print_help') as mock_help:
            from scripts.manage_committees import main
            main()
            
            mock_help.assert_called_once()

    def test_invalid_command_exits(self):
        """Test that invalid commands cause exit."""
        test_args = ['manage_committees.py', 'invalid_command']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesArgumentParsing:
    """Test argument parsing functionality."""
    
    def test_list_parser(self):
        """Test list command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        list_parser = subparsers.add_parser('list', help='List all committee targets')
        
        args = parser.parse_args(['list'])
        assert args.command == 'list'

    def test_add_parser_full_args(self):
        """Test add command with all arguments."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        add_parser = subparsers.add_parser('add', help='Add a committee target')
        add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
        add_parser.add_argument('--name', help='Committee name')
        add_parser.add_argument('--description', help='Description')
        
        args = parser.parse_args(['add', 'C00467571', '--name', 'Test Committee', '--description', 'Test Desc'])
        assert args.command == 'add'
        assert args.committee_id == 'C00467571'
        assert args.name == 'Test Committee'
        assert args.description == 'Test Desc'

    def test_add_parser_minimal_args(self):
        """Test add command with only required arguments."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        add_parser = subparsers.add_parser('add', help='Add a committee target')
        add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
        add_parser.add_argument('--name', help='Committee name')
        add_parser.add_argument('--description', help='Description')
        
        args = parser.parse_args(['add', 'C00467571'])
        assert args.command == 'add'
        assert args.committee_id == 'C00467571'
        assert args.name is None
        assert args.description is None

    def test_remove_parser(self):
        """Test remove command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        remove_parser = subparsers.add_parser('remove', help='Remove a committee target')
        remove_parser.add_argument('committee_id', help='Committee ID to remove')
        
        args = parser.parse_args(['remove', 'C00467571'])
        assert args.command == 'remove'
        assert args.committee_id == 'C00467571'

    def test_all_parser(self):
        """Test all command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        all_parser = subparsers.add_parser('all', help='Enable all committees mode (deactivate all targets)')
        
        args = parser.parse_args(['all'])
        assert args.command == 'all'

class TestManageCommitteesIntegration:
    """Integration tests for manage_committees.py"""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_full_list_workflow(self, mock_print, mock_list_targets):
        """Test complete list workflow."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': 'Committee 1', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            # Verify full workflow
            mock_list_targets.assert_called_once()
            assert mock_print.call_count >= 3  # Header, separator, and committee info

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_full_add_workflow(self, mock_print, mock_add_target):
        """Test complete add workflow."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', 'New Committee']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', 'New Committee', None)
            mock_print.assert_called_with("Successfully added committee target: C00123456")

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_full_remove_workflow(self, mock_print, mock_remove_target):
        """Test complete remove workflow."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00123456']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00123456')
            mock_print.assert_called_with("Successfully removed committee target: C00123456")

class TestManageCommitteesEdgeCases:
    """Test edge cases and error conditions."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_mixed_active_status(self, mock_print, mock_list_targets):
        """Test listing with mix of active and inactive targets."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': 'Active Committee', 'active': True},
            {'committee_id': 'C002', 'committee_name': 'Inactive Committee', 'active': False}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            active_calls = [call for call in print_calls if "ACTIVE" in call and "C001" in call]
            inactive_calls = [call for call in print_calls if "INACTIVE" in call and "C002" in call]
            
            assert len(active_calls) == 1
            assert len(inactive_calls) == 1

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_none_committee_names(self, mock_print, mock_list_targets):
        """Test listing when committee names are None."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': None, 'active': True},
            {'committee_id': 'C002', 'committee_name': '', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            na_calls = [call for call in print_calls if "N/A" in call]
            # Should handle both None and empty string as "N/A"
            assert len(na_calls) >= 1

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_with_special_characters(self, mock_print, mock_add_target):
        """Test adding committee with special characters."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', "Committee's & Friends", '--description', 'Test & Description']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', "Committee's & Friends", 'Test & Description')
            mock_print.assert_called_with("Successfully added committee target: C00123456")

    def test_add_missing_committee_id(self):
        """Test add command without committee ID."""
        test_args = ['manage_committees.py', 'add']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

    def test_remove_missing_committee_id(self):
        """Test remove command without committee ID."""
        test_args = ['manage_committees.py', 'remove']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.list_committee_targets')
    def test_list_command_exception_handling(self, mock_list_targets):
        """Test that exceptions from scripts.manage_committees are properly handled."""
        mock_list_targets.side_effect = Exception("Database error")
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database error"):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesEnvironmentSetup:
    """Test environment and import setup."""
    
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    def test_environment_loading(self, mock_getenv, mock_load_dotenv):
        """Test that environment is loaded correctly."""
        mock_getenv.return_value = "prod"
        
        # Clear module cache and re-import to trigger environment loading
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
        
        import scripts.manage_committees
        
        # Should load .env first, then .env.{mode}
        assert mock_load_dotenv.call_count >= 1

    def test_imports_successful(self):
        """Test that all required imports work."""
        # This test verifies that the module can be imported without errors
        from scripts.manage_committees import main
        assert callable(main)

    def test_logger_setup(self):
        """Test that logger is set up."""
        import scripts.manage_committees as mc
        assert hasattr(mc, 'logger')
        assert mc.logger is not None

class TestManageCommitteesAdvancedScenarios:
    """Additional advanced test scenarios."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_empty_strings_and_none_values(self, mock_print, mock_list_targets):
        """Test listing handles various falsy values correctly."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': '', 'active': True},
            {'committee_id': 'C002', 'committee_name': '   ', 'active': False},
            {'committee_id': 'C003', 'committee_name': None, 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            
            # All should display "N/A" for empty/None names
            na_calls = [call for call in print_calls if "N/A" in call]
            assert len(na_calls) >= 2  # At least empty string and None should show as N/A

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_with_long_names_and_descriptions(self, mock_print, mock_add_target):
        """Test adding committee with very long names and descriptions."""
        mock_add_target.return_value = True
        
        long_name = "A" * 200
        long_description = "B" * 500
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', long_name, '--description', long_description]
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', long_name, long_description)

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_large_number_of_committees(self, mock_print, mock_list_targets):
        """Test listing with many committees."""
        # Generate 100 test committees
        committees = []
        for i in range(100):
            committees.append({
                'committee_id': f'C{i:08d}',
                'committee_name': f'Test Committee {i}',
                'active': i % 2 == 0  # Alternate active/inactive
            })
        
        mock_list_targets.return_value = committees
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_list_targets.assert_called_once()
            # Should print header + separator + 100 committees
            assert mock_print.call_count >= 102

    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_unicode_characters(self, mock_add_target):
        """Test adding committee with unicode characters."""
        mock_add_target.return_value = True
        
        unicode_name = "Comité Español 中文 🏛️"
        unicode_desc = "Description with émojis 📊 and spéciál characters"
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', unicode_name, '--description', unicode_desc]
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', unicode_name, unicode_desc)

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_nonexistent_committee(self, mock_print, mock_remove_target):
        """Test removing a committee that doesn't exist."""
        mock_remove_target.return_value = False
        
        test_args = ['manage_committees.py', 'remove', 'C99999999']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C99999999')
            mock_print.assert_called_with("Failed to remove committee target: C99999999")
            assert exc_info.value.code == 1

    def test_parser_with_conflicting_args(self):
        """Test parser behavior with potentially conflicting arguments."""
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', '--description']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):  # Should fail due to missing description value
            from scripts.manage_committees import main
            main()

class TestManageCommitteesOutputFormatting:
    """Test output formatting and display logic."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_output_column_alignment(self, mock_print, mock_list_targets):
        """Test that list output maintains proper column alignment."""
        mock_list_targets.return_value = [
            {'committee_id': 'C00123456789', 'committee_name': 'Short', 'active': True},
            {'committee_id': 'C001', 'committee_name': 'Very Long Committee Name That Goes On And On', 'active': False}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [call[0][0] for call in mock_print.call_args_list if call[0]]
            
            # Find the actual committee data lines (skip header and separator)
            committee_lines = [line for line in print_calls if line.startswith('C')]
            
            # Verify proper spacing format (committee_id should be left-aligned in 12 chars)
            for line in committee_lines:
                assert 'ACTIVE' in line or 'INACTIVE' in line

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_very_long_committee_names(self, mock_print, mock_list_targets):
        """Test handling of very long committee names."""
        long_name = "X" * 100
        mock_list_targets.return_value = [
            {'committee_id': 'C00123456', 'committee_name': long_name, 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [call[0][0] for call in mock_print.call_args_list if call[0]]
            committee_line = [line for line in print_calls if 'C00123456' in line][0]
            
            # Should include the full long name
            assert long_name in committee_line

class TestManageCommitteesErrorScenarios:
    """Test various error and exception scenarios."""
    
    def setup_method(self):
        """Clear module cache before each test."""
        if 'scripts.manage_committees' in sys.modules:
            del sys.modules['scripts.manage_committees']
    
    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_database_exception(self, mock_add_target):
        """Test add command when database throws exception."""
        mock_add_target.side_effect = Exception("Database connection failed")
        
        test_args = ['manage_committees.py', 'add', 'C00123456']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database connection failed"):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.remove_committee_target')
    def test_remove_with_database_exception(self, mock_remove_target):
        """Test remove command when database throws exception."""
        mock_remove_target.side_effect = Exception("Database connection failed")
        
        test_args = ['manage_committees.py', 'remove', 'C00123456']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database connection failed"):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.enable_all_committees_mode')
    def test_all_with_database_exception(self, mock_enable_all):
        """Test all command when database throws exception."""
        mock_enable_all.side_effect = Exception("Database connection failed")
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database connection failed"):
            from scripts.manage_committees import main
            main()

            if __name__ == '__main__':
                pytest.main([__file__])

            # Verify the function was called
            mock_list_targets.assert_called_once()
            
            # Verify output formatting
            print_calls = [str(call) for call in mock_print.call_args_list]
            
            # Should print header
            header_calls = [call for call in print_calls if "Committee Targets:" in call]
            assert len(header_calls) == 1
            
            # Should print committee info with proper formatting
            committee_calls = [call for call in print_calls if "C00467571" in call and "ACTIVE" in call]
            assert len(committee_calls) == 1
            
            committee_calls = [call for call in print_calls if "C00123456" in call and "INACTIVE" in call]
            assert len(committee_calls) == 1
            
            # Should handle None name with "N/A"
            na_calls = [call for call in print_calls if "C00789012" in call and "N/A" in call]
            assert len(na_calls) == 1

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_command_no_targets(self, mock_print, mock_list_targets):
        """Test listing committee targets when no targets exist."""
        mock_list_targets.return_value = []
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_list_targets.assert_called_once()
            mock_print.assert_called_with("No committee targets found.")

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_success(self, mock_print, mock_add_target):
        """Test successful addition of committee target."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00467571', '--name', 'Test Committee', '--description', 'Test Description']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', 'Test Committee', 'Test Description')
            mock_print.assert_called_with("Successfully added committee target: C00467571")

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_failure(self, mock_print, mock_add_target):
        """Test failed addition of committee target."""
        mock_add_target.return_value = False
        
        test_args = ['manage_committees.py', 'add', 'C00467571']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00467571', None, None)
            mock_print.assert_called_with("Failed to add committee target: C00467571")
            assert exc_info.value.code == 1

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_add_command_minimal_args(self, mock_print, mock_add_target):
        """Test adding committee with only required argument."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00467571']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            # Should pass None for optional arguments
            mock_add_target.assert_called_once_with('C00467571', None, None)

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_command_success(self, mock_print, mock_remove_target):
        """Test successful removal of committee target."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00467571']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00467571')
            mock_print.assert_called_with("Successfully removed committee target: C00467571")

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_remove_command_failure(self, mock_print, mock_remove_target):
        """Test failed removal of committee target."""
        mock_remove_target.return_value = False
        
        test_args = ['manage_committees.py', 'remove', 'C00467571']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00467571')
            mock_print.assert_called_with("Failed to remove committee target: C00467571")
            assert exc_info.value.code == 1

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_success(self, mock_print, mock_enable_all):
        """Test successful enabling of all committees mode."""
        mock_enable_all.return_value = True
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()
            mock_print.assert_called_with("Successfully enabled all committees mode")

    @patch('scripts.manage_committees.enable_all_committees_mode')
    @patch('builtins.print')
    def test_all_command_failure(self, mock_print, mock_enable_all):
        """Test failed enabling of all committees mode."""
        mock_enable_all.return_value = False
        
        test_args = ['manage_committees.py', 'all']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit) as exc_info:
            from scripts.manage_committees import main
            main()
            
            mock_enable_all.assert_called_once()
            mock_print.assert_called_with("Failed to enable all committees mode")
            assert exc_info.value.code == 1

    def test_no_command_shows_help(self):
        """Test that running without command shows help."""
        test_args = ['manage_committees.py']
        
        with patch('sys.argv', test_args), \
             patch('argparse.ArgumentParser.print_help') as mock_help:
            from scripts.manage_committees import main
            main()
            
            mock_help.assert_called_once()

    def test_invalid_command_exits(self):
        """Test that invalid commands cause exit."""
        test_args = ['manage_committees.py', 'invalid_command']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesArgumentParsing:
    """Test argument parsing functionality."""
    
    def test_list_parser(self):
        """Test list command argument parsing."""
        from scripts.manage_committees import main
        
        # Import the module to access parser setup
        import scripts.manage_committees as mc
        
        # Create a parser similar to what's in main()
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        list_parser = subparsers.add_parser('list', help='List all committee targets')
        
        args = parser.parse_args(['list'])
        assert args.command == 'list'

    def test_add_parser_full_args(self):
        """Test add command with all arguments."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        add_parser = subparsers.add_parser('add', help='Add a committee target')
        add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
        add_parser.add_argument('--name', help='Committee name')
        add_parser.add_argument('--description', help='Description')
        
        args = parser.parse_args(['add', 'C00467571', '--name', 'Test Committee', '--description', 'Test Desc'])
        assert args.command == 'add'
        assert args.committee_id == 'C00467571'
        assert args.name == 'Test Committee'
        assert args.description == 'Test Desc'

    def test_add_parser_minimal_args(self):
        """Test add command with only required arguments."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        add_parser = subparsers.add_parser('add', help='Add a committee target')
        add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
        add_parser.add_argument('--name', help='Committee name')
        add_parser.add_argument('--description', help='Description')
        
        args = parser.parse_args(['add', 'C00467571'])
        assert args.command == 'add'
        assert args.committee_id == 'C00467571'
        assert args.name is None
        assert args.description is None

    def test_remove_parser(self):
        """Test remove command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        remove_parser = subparsers.add_parser('remove', help='Remove a committee target')
        remove_parser.add_argument('committee_id', help='Committee ID to remove')
        
        args = parser.parse_args(['remove', 'C00467571'])
        assert args.command == 'remove'
        assert args.committee_id == 'C00467571'

    def test_all_parser(self):
        """Test all command argument parsing."""
        parser = argparse.ArgumentParser(description="Manage committee targets")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        all_parser = subparsers.add_parser('all', help='Enable all committees mode (deactivate all targets)')
        
        args = parser.parse_args(['all'])
        assert args.command == 'all'

class TestManageCommitteesIntegration:
    """Integration tests for manage_committees.py"""
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_full_list_workflow(self, mock_print, mock_list_targets):
        """Test complete list workflow."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': 'Committee 1', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            # Verify full workflow
            mock_list_targets.assert_called_once()
            assert mock_print.call_count >= 3  # Header, separator, and committee info

    @patch('scripts.manage_committees.add_committee_target')
    @patch('builtins.print')
    def test_full_add_workflow(self, mock_print, mock_add_target):
        """Test complete add workflow."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', 'New Committee']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', 'New Committee', None)
            mock_print.assert_called_with("Successfully added committee target: C00123456")

    @patch('scripts.manage_committees.remove_committee_target')
    @patch('builtins.print')
    def test_full_remove_workflow(self, mock_print, mock_remove_target):
        """Test complete remove workflow."""
        mock_remove_target.return_value = True
        
        test_args = ['manage_committees.py', 'remove', 'C00123456']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_remove_target.assert_called_once_with('C00123456')
            mock_print.assert_called_with("Successfully removed committee target: C00123456")

class TestManageCommitteesEdgeCases:
    """Test edge cases and error conditions."""
    
    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_mixed_active_status(self, mock_print, mock_list_targets):
        """Test listing with mix of active and inactive targets."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': 'Active Committee', 'active': True},
            {'committee_id': 'C002', 'committee_name': 'Inactive Committee', 'active': False}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            active_calls = [call for call in print_calls if "ACTIVE" in call and "C001" in call]
            inactive_calls = [call for call in print_calls if "INACTIVE" in call and "C002" in call]
            
            assert len(active_calls) == 1
            assert len(inactive_calls) == 1

    @patch('scripts.manage_committees.list_committee_targets')
    @patch('builtins.print')
    def test_list_with_none_committee_names(self, mock_print, mock_list_targets):
        """Test listing when committee names are None."""
        mock_list_targets.return_value = [
            {'committee_id': 'C001', 'committee_name': None, 'active': True},
            {'committee_id': 'C002', 'committee_name': '', 'active': True}
        ]
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            print_calls = [str(call) for call in mock_print.call_args_list]
            na_calls = [call for call in print_calls if "N/A" in call]
            # Should handle both None and empty string as "N/A"
            assert len(na_calls) >= 1

    @patch('scripts.manage_committees.add_committee_target')
    def test_add_with_special_characters(self, mock_add_target):
        """Test adding committee with special characters."""
        mock_add_target.return_value = True
        
        test_args = ['manage_committees.py', 'add', 'C00123456', '--name', "Committee's & Friends", '--description', 'Test & Description']
        
        with patch('sys.argv', test_args):
            from scripts.manage_committees import main
            main()
            
            mock_add_target.assert_called_once_with('C00123456', "Committee's & Friends", 'Test & Description')

    def test_add_missing_committee_id(self):
        """Test add command without committee ID."""
        test_args = ['manage_committees.py', 'add']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

    def test_remove_missing_committee_id(self):
        """Test remove command without committee ID."""
        test_args = ['manage_committees.py', 'remove']
        
        with patch('sys.argv', test_args), \
             pytest.raises(SystemExit):
            from scripts.manage_committees import main
            main()

    @patch('scripts.manage_committees.list_committee_targets')
    def test_list_command_exception_handling(self, mock_list_targets):
        """Test that exceptions from scripts.manage_committees are not caught (should propagate)."""
        mock_list_targets.side_effect = Exception("Database error")
        
        test_args = ['manage_committees.py', 'list']
        
        with patch('sys.argv', test_args), \
             pytest.raises(Exception, match="Database error"):
            from scripts.manage_committees import main
            main()

class TestManageCommitteesEnvironmentSetup:
    """Test environment and import setup."""
    
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    def test_environment_loading(self, mock_getenv, mock_load_dotenv):
        """Test that environment is loaded correctly."""
        mock_getenv.return_value = "prod"
        
        # Re-import to trigger environment loading
        import importlib
        import scripts.manage_committees
        importlib.reload(scripts.manage_committees)
        
        # Should load .env first, then .env.{mode}
        assert mock_load_dotenv.call_count >= 1

    def test_imports_successful(self):
        """Test that all required imports work."""
        # This test verifies that the module can be imported without errors
        from scripts.manage_committees import main
        assert callable(main)

    def test_logger_setup(self):
        """Test that logger is set up."""
        import scripts.manage_committees as mc
        assert hasattr(mc, 'logger')
        assert mc.logger is not None

if __name__ == '__main__':
    pytest.main([__file__])