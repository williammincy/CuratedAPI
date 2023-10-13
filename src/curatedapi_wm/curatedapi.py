import requests
import json


class CuratedLink:
    def __init__(self, url, title=None, description=None, image=None, category=None, id=None):
        """
        Represents a curated link.

        Parameters:
            url (str): The URL of the link.
            title (str, optional): The title of the link.
            description (str, optional): The description of the link.
            image (str, optional): The image URL associated with the link.
            category (str, optional): The category of the link.
            id (str, optional): Local identifier for the CuratedLink instance.
        """
        self.url = url
        self.title = title
        self.description = description
        self.image = image
        self.category = category
        self.id = id

    def __str__(self):
        """Returns a string representation of the CuratedLink."""
        return f"Title: {self.title}\nURL: {self.url}\nDescription: {self.description}\nCategory: {self.category}\nID: {self.id}\n"

    @classmethod
    def from_json(cls, json_data):
        """
        Create a new instance of CuratedLink based on a JSON object.

        Parameters:
            json_data (dict): A JSON object containing data for CuratedLink attributes.

        Returns:
            CuratedLink: A new instance of CuratedLink with data from the JSON object.
        """
        return cls(
            url=json_data.get("url"),
            title=json_data.get("title"),
            description=json_data.get("description"),
            image=json_data.get("image_url"),
            category=json_data.get("category"),
            id=json_data.get("id")
        )

    def to_json(self):
        """
        Return the object as JSON.

        Returns:
            str: JSON representation of the CuratedLink instance.
        """
        link_data = {
            "url": self.url,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "category": self.category,
            "id": self.id
        }
        return json.dumps(link_data)


class CuratedCategory:
    def __init__(self, code=None, name=None, sponsored=False, limit=None):
        self.code = code
        self.name = name
        self.sponsored = sponsored
        self.limit = limit

    def __str__(self):
        return f"Code: {self.code}\nName: {self.name}\nSponsored: {self.sponsored}\nLimit: {self.limit}\n"

    @classmethod
    def from_json(cls, json_data):
        """
        Create a new instance of CuratedCategory from JSON data.

        Parameters:
            json_data (dict): JSON data containing 'code', 'name', 'sponsored', and 'limit' attributes.

        Returns:
            CuratedCategory: New instance of CuratedCategory.
        """
        return cls(
            code=json_data.get("code"),
            name=json_data.get("name"),
            sponsored=json_data.get("sponsored", False),
            limit=json_data.get("limit")
        )

    def to_json(self):
        """
        Return the object as JSON.

        Returns:
            str: JSON representation of the CuratedCategory instance.
        """
        category_data = {
            "code": self.code,
            "name": self.name,
            "sponsored": self.sponsored,
            "limit": self.limit
        }
        return json.dumps(category_data)


class CuratedApi:
    def __init__(self, api_key):
        """
        Initialize the CuratedApi class with the provided API key.

        Parameters:
            api_key (str): The API key to authenticate requests.
        """
        self.base_url = "https://api.curated.co/api/v3"
        self.api_key = api_key
        self.publication_id = None

    def get_base_url(self):
        """Returns the base string for a URL."""
        return self.base_url

    def get_api_key(self):
        """Returns the API key."""
        return self.api_key

    def set_publication_id(self, publication_id):
        """
        Sets the publication ID.

        Parameters:
            publication_id (str): The ID of the publication.
        """
        self.publication_id = publication_id

    def get_categories_url(self, publication_id=None):
        """
        Returns the URL for accessing categories for the specified publication or the stored publication ID.

        Parameters:
            publication_id (str, optional): The ID of the publication.

        Returns:
            str: The concatenated URL string.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        base_url = self.get_base_url()
        categories_url = f"{base_url}/publications/{self.publication_id}/categories"
        return categories_url

    def get_publication_links_url(self):
        """
        Returns the publication link URL for the stored publication ID.

        Returns:
            str: The concatenated URL string.
        """
        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        publication_url = f"{self.base_url}/publications/{self.publication_id}/links"
        return publication_url
    
    def get_publication_issues_url(self):
        """
        Returns the publication issues URL for the stored publication ID.

        Returns:
            str: The concatenated URL string.
        """
        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        issues_url = f"{self.base_url}/publications/{self.publication_id}/issues"
        return issues_url

    def get_publications_url(self):
        """
        Returns the URL for getting publication IDs.

        Returns:
            str: The concatenated URL string.
        """
        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        publication_url = f"{self.base_url}/publications"
        return publication_url

    def get_links_url(self, publication_id=None):
        """
        Returns the URL for getting link not associated with a publication

        Parameters:
            link_id (str): The ID of the link.
            publication_id (str, optional): The ID of the publication.

        Returns:
            str: The concatenated URL string.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        links_url = f"{self.base_url}/publications/{self.publication_id}/links"
        return links_url

    def get_link_url(self, link_id, publication_id=None):
        """
        Returns the URL for the specified link ID and optionally the publication ID.

        Parameters:
            link_id (str): The ID of the link.
            publication_id (str, optional): The ID of the publication.

        Returns:
            str: The concatenated URL string.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        link_url = f"{self.base_url}/publications/{self.publication_id}/links/{link_id}"
        return link_url

    def get_request_headers(self):
        """Returns the headers required for API requests."""
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "Authorization": f'Token token="{self.api_key}"'
        }
        return headers

    def request_all_publications(self, publication_id=None):
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        url = self.get_publications_url()
        headers = self.get_request_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            publication_data = response.json()
            return publication_data
        else:
            response.raise_for_status()

    def request_all_categories(self, publication_id=None):
        """
        Requests all categories from the publication using a GET HTTP request.

        Parameters:
            publication_id (str, optional): The ID of the publication.

        Returns:
            list: A list of CuratedCategory instances representing the categories.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        url = self.get_categories_url()
        headers = self.get_request_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            categories_data = response.json()
            categories = [CuratedCategory.from_json(
                category_data) for category_data in categories_data]
            return categories
        else:
            response.raise_for_status()

    def request_all_links(self, publication_id=None):
        """
        Sends a GET request to retrieve all links from the specified publication or the stored publication ID.

        Parameters:
            publication_id (str, optional): The ID of the publication.

        Returns:
            dict: JSON response containing the links data.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        url = self.get_links_url()
        headers = self.get_request_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            links_data = response.json()
            links = [CuratedLink.from_json(link_data)
                     for link_data in links_data]
            return links
        else:
            response.raise_for_status()

    def request_specific_link(self, link_id, publication_id=None):
        """
        Sends a GET request to retrieve a specific link from the specified publication or the stored publication ID.

        Parameters:
            link_id (str): The ID of the link.
            publication_id (str, optional): The ID of the publication.

        Returns:
            CuratedLink: An instance of the CuratedLink class representing the specific link.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        url = self.get_link_url(link_id, self.publication_id)
        headers = self.get_request_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            link_data = response.json()
            curated_link = CuratedLink.from_json(link_data)
            return curated_link
        else:
            response.raise_for_status()

    def create_curated_link(self, curated_link):
        """
        Creates a new curated link by sending a POST request to the publication URL.

        Parameters:
            curated_link (CuratedLink): An instance of the CuratedLink class representing the link to create.

        Raises:
            ValueError: If the URL or title of the CuratedLink instance is None.

        Returns:
            dict: JSON response containing the newly created link data.
        """
        if curated_link.url is None:
            raise ValueError("URL of the CuratedLink instance cannot be None.")
        if curated_link.title is None:
            raise ValueError(
                "Title of the CuratedLink instance cannot be None.")

        url = self.get_links_url()
        headers = self.get_request_headers()
        query = "?url=" + curated_link.url + "&title=" + curated_link.title + \
            "&description='" + curated_link.description + "'&image=" + \
                curated_link.image + "&category=" + curated_link.category

        response = requests.post(url+query, headers=headers)

        if response.status_code == 201:
            response_data = response.json()
            curated_link = CuratedLink.from_json(response_data)
            return curated_link
        else:
            print(response)
            response.raise_for_status()

    def delete_specific_link(self, link_id, publication_id=None):
        """
        Sends a DELETE request to remove a specific link from the specified publication or the stored publication ID.

        Parameters:
            link_id (str): The ID of the link to delete.
            publication_id (str, optional): The ID of the publication.

        Returns:
            str: A message indicating the success of the deletion.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        url = self.get_link_url(link_id, self.publication_id)
        headers = self.get_request_headers()

        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            return "Link deletion successful."
        elif response.status_code == 404:
            return "Link not found."
        else:
            response.raise_for_status()

    def update_specific_link(self, curated_link, publication_id=None):
        """
        Updates a specific curated link using a PUT HTTP request.

        Parameters:
            curated_link (CuratedLink): The CuratedLink instance to be updated.
            publication_id (str, optional): The ID of the publication.

        Returns:
            CuratedLink: The updated CuratedLink instance.
        """
        if publication_id:
            self.publication_id = publication_id

        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        if not curated_link.id:
            raise ValueError("CuratedLink's id has not been set.")

        url = self.get_link_url(curated_link.id)
        headers = self.get_request_headers()
        payload = curated_link.to_json()

        response = requests.put(url, headers=headers, data=payload)

        if response.status_code == 200:
            link_data = response.json()
            # updated_link = CuratedLink.from_json(link_data)
            return link_data
        else:
            response.raise_for_status()
