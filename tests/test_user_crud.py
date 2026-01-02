import pytest

@pytest.mark.usefixtures("api_client")
class TestUserCRUD:
    
    def test_create_user(self):
        print("\n--- 1. Create User ---")
        payload = {
            "name": "John SDET",
            "username": "john_sdet",
            "email": "john@automation.com"
        }
        
        response = self.client.post("/users", payload)
        
        # Validation
        assert response.status_code == 201  # 201 Created
        json_data = response.json()
        print(f"Response: {json_data}")
        
        # JSONPlaceholder always returns ID 11 for new posts
        assert json_data["id"] == 11
        assert json_data["name"] == "John SDET"

    def test_get_user_list(self):
        print("\n--- 2. Get User List ---")
        response = self.client.get("/users")
        
        assert response.status_code == 200
        json_data = response.json()
        
        # Verify we got 10 users (Standard for this API)
        assert len(json_data) == 10
        print("User list fetched successfully")

    def test_update_user(self):
        print("\n--- 3. Update User ---")
        # We will update User ID 1
        user_to_update = "1" 
        
        payload = {
            "name": "Leanne Graham Updated",
            "email": "updated@test.com"
        }
        
        response = self.client.put(f"/users/{user_to_update}", payload)
        
        assert response.status_code == 200
        json_data = response.json()
        print(f"Update Response: {json_data}")
        
        assert json_data["name"] == "Leanne Graham Updated"

    def test_delete_user(self):
        print("\n--- 4. Delete User ---")
        user_to_delete = "1"
        
        response = self.client.delete(f"/users/{user_to_delete}")
        
        # JSONPlaceholder returns 200 for delete (ReqRes returned 204)
        assert response.status_code == 200
        print("User deleted successfully")