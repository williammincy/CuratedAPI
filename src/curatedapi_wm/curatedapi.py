import requests
import json
from urllib.parse import urlencode


class CuratedLink:
    def __init__(self, url:str, title:str=None, description:str=None, image:str=None, category:str=None, id:int=None):
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
    def __init__(self, code:str=None, name:str=None, sponsored:bool=False, limit:int=None):
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

class CuratedIssuesResponse:
    def __init__(self, page:int, total_pages:int, total_results:int, data:dict):
        """
        Represents a curated issue response.

        Parameters:
            page (int): The page number for the data returned in this call.
            total_pages (int):  How many pages are available using this page size.
            total_results (int): The total number of results which are available.
            data (dict): A dictionary of CuratedIssue instances.
        """
        self.page = page
        self.total_pages = total_pages
        self.total_results = total_results 
        self.data = data

    def __str__(self):
        """Returns a string representation of the CuratedLink."""
        return f"Page: {self.page}\nTotal Pages: {self.total_pages}\nTotal Results: {self.total_results}\nData: {self.data}\n"

    @classmethod
    def from_json(cls, json_data):
        """
        Create a new instance of CuratedIssuesResponse based on a JSON object.

        Parameters:
            json_data (dict): A JSON object containing data for CuratedIssuesResponse attributes.

        Returns:
            CuratedIssuesResponse: A new instance of CuratedIssuesResponse with data from the JSON object.
        """
        return cls(
            page=json_data.get("page"),
            total_pages=json_data.get("total_pages"),
            total_results=json_data.get("total_results"),
            data=[CuratedIssue.from_json(issue)
                    for issue in json_data.get("data")]
        )

    def to_json(self):
        """
        Return the object as JSON.

        Returns:
            str: JSON representation of the CuratedIssuesResponse instance.
        """
        link_data = {
            "page": self.page,
            "total_pages": self.total_pages,
            "total_results": self.total_results,
            "data": [CuratedIssue.from_json(issue)
                     for issue in self.data]
        }
        return json.dumps(link_data)

class CuratedIssue:
    def __init__(self, id:int, number:int, published_at:str=None, summary:str=None, url:str=None, updated_at :str=None):
        """
        Represents a curated link.

        Parameters:
            id (int): Local identifier for the issue instance.
            number (int): The issue number.
            published_at (str, optional): The date that the issue was published in ISO 8601 format.
            summary (str, optional): The summary for the issue instance.
            url (str, optional): The public URL associated with the issue.
            updated_at (str, optional): The date that the issue was last updated (may be after publishing) in ISO 8601 format.
        """
        self.id = id
        self.number = number
        self.published_at = published_at
        self.summary = summary
        self.url  = url 
        self.updated_at = updated_at

    def __str__(self):
        """Returns a string representation of the CuratedIssue."""
        return f"ID: {self.id}\nIssue Number: {self.number}\nSummary: {self.summary}\nURL: {self.url}\Published Date: {self.published_at}\Last nUpdated: {self.updated_at}\n"

    @classmethod
    def from_json(cls, json_data):
        """
        Create a new instance of CuratedIssue based on a JSON object.

        Parameters:
            json_data (dict): A JSON object containing data for CuratedIssue attributes.

        Returns:
            CuratedIssue: A new instance of CuratedIssue with data from the JSON object.
        """
        return cls(
            id=json_data.get("id"),
            number=json_data.get("number"),
            published_at=json_data.get("published_at"),
            summary=json_data.get("summary"),
            url=json_data.get("url"),
            updated_at=json_data.get("updated_at")
        )

    def to_json(self):
        """
        Return the object as JSON.

        Returns:
            str: JSON representation of the CuratedIssue instance.
        """
        link_data = {
            "id": self.id,
            "number": self.number,
            "published_at": self.published_at,
            "summary": self.summary,
            "url": self.url,
            "updated_at": self.updated_at
        }
        return json.dumps(link_data)


class CuratedApi:
    def __init__(self, api_key:str):
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

    def set_publication_id(self, publication_id:int):
        """
        Sets the publication ID.

        Parameters:
            publication_id (str): The ID of the publication.
        """
        self.publication_id = publication_id

    def get_categories_url(self):
        """
        Returns the URL for accessing categories for the specified publication or the stored publication ID.

        Returns:
            str: The concatenated URL string.
        """

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
    
    def get_email_subscribers_url(self):
        """
        Returns the email subscribers URL for the stored publication ID.

        Returns:
            str: The concatenated URL string.
        """
        if not self.publication_id:
            raise ValueError("Publication ID has not been set.")

        subscribers_url = f"{self.base_url}/publications/{self.publication_id}/email_unsubscribers"
        return subscribers_url
    
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

    def get_links_url(self):
        """
        Returns the URL for getting link not associated with a publication

        Parameters:
            link_id (str): The ID of the link.

        Returns:
            str: The concatenated URL string.
        """
        links_url = f"{self.base_url}/publications/{self.publication_id}/links"
        return links_url

    def get_link_url(self, link_id:int):
        """
        Returns the URL for the specified link ID and optionally the publication ID.

        Parameters:
            link_id (str): The ID of the link.

        Returns:
            str: The concatenated URL string.
        """
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

    def request_all_publications(self):
        url = self.get_publications_url()
        headers = self.get_request_headers()
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            publication_data = response.json()
            return publication_data
        else:
            response.raise_for_status()

    def request_all_categories(self):
        """
        Requests all categories from the publication using a GET HTTP request.

        Returns:
            list: A list of CuratedCategory instances representing the categories.
        """
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

    def request_all_links(self):
        """
        Sends a GET request to retrieve all links from the specified publication or the stored publication ID.

        Returns:
            dict: JSON response containing the links data.
        """
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
            
    def request_all_subscribers(self):
        """
        Sends a GET request to retrieve all email subscribers from the specified publication or the stored publication ID.

        Returns:
            dict: JSON response containing the links data.
        """
        url = self.get_email_subscribers_url()
        headers = self.get_request_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            links_data = response.json()
            return links_data
        else:
            response.raise_for_status()

    def request_specific_link(self, link_id:int):
        """
        Sends a GET request to retrieve a specific link from the specified publication or the stored publication ID.

        Parameters:
            link_id (str): The ID of the link.

        Returns:
            CuratedLink: An instance of the CuratedLink class representing the specific link.
        """
        url = self.get_link_url(link_id, self.publication_id)
        headers = self.get_request_headers()

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            link_data = response.json()
            curated_link = CuratedLink.from_json(link_data)
            return curated_link
        else:
            response.raise_for_status()

    def create_curated_link(self, curated_link:CuratedLink):
        """
        Creates a new curated link by sending a POST request to the publication URL.

        Parameters:
            curated_link (CuratedLink): An instance of the CuratedLink class representing the link to create.

        Raises:
            ValueError: If the URL of the CuratedLink instance is None.

        Returns:
            CuratedLink: The newly created link data as an instance of CuratedLink.
        """
        if curated_link.url is None:
            raise ValueError("URL of the CuratedLink instance cannot be None.")

        url = self.get_links_url()
        headers = self.get_request_headers()

        query = "?" + urlencode(curated_link.to_json)

        response = requests.post(url + query, headers=headers)

        if response.status_code == 201:
            response_data = response.json()
            curated_link = CuratedLink.from_json(response_data)
            return curated_link
        else:
            print(response)
            response.raise_for_status()

    def subscribe_email(self, email:str, sync:bool=False):
        """
        Creates a new curated link by sending a POST request to the publication URL.

        Parameters:
            email (str): Email address we want to subscribe to the publication.
            sync (bool, optional): Set to true to bypass double opt-in settings, default is False

        Raises:
            ValueError: If the email is None.

        Returns:
            dict: JSON response containing the newly subscriber email data.
        """
        if email is None:
            raise ValueError("email cannot be None.")
        
        url = self.get_email_subscribers_url()
        headers = self.get_request_headers()
        data = {
            "email": email,
            "sync": sync
        }

        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            return response.json()
        else:
            print(response)
            response.raise_for_status()

    def delete_specific_link(self, link_id:int):
        """
        Sends a DELETE request to remove a specific link from the specified publication or the stored publication ID.

        Parameters:
            link_id (str): The ID of the link to delete.

        Returns:
            str: A message indicating the success of the deletion.
        """
        url = self.get_link_url(link_id, self.publication_id)
        headers = self.get_request_headers()

        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            return "Link deletion successful."
        elif response.status_code == 404:
            return "Link not found."
        else:
            response.raise_for_status()

    def update_specific_link(self, curated_link:CuratedLink):
        """
        Updates a specific curated link using a PUT HTTP request.

        Parameters:
            curated_link (CuratedLink): The CuratedLink instance to be updated.

        Returns:
            CuratedLink: The updated CuratedLink instance.
        """
        if not curated_link.id:
            raise ValueError("CuratedLink's id has not been set.")

        url = self.get_link_url(curated_link.id)
        headers = self.get_request_headers()
        payload = curated_link.to_json()

        response = requests.put(url, headers=headers, data=payload)

        if response.status_code == 200:
            link_data = response.json()
            return link_data
        else:
            response.raise_for_status()

    def request_all_issues(self, per_page:int=10, state:str="draft", page:int=None, stats:bool=False):
        """
        Sends a GET request to retrieve all links from the specified publication or the stored publication ID.

        Parameters:
            per_page (int, optional): Total issues returned per page, maximum 250.
            state (str, optional): Status of issues returned, defaults to returneing "draft" issues .
            page (int, optional): Current page within total number of issues.
            stats (bool, optional): Should issue stats be returned with responses, defaults to False.

        Returns:
            dict: JSON response containing the links data.
        """
        url = self.get_publication_issues_url()
        headers = self.get_request_headers()
        query = "?per_page=" + per_page + "&state=" + state + \
            "&stats='" + stats
        if page is not None:
            query = query + "&page=" + page

        response = requests.get(url + query, headers=headers)

        if response.status_code == 200:
            links_data = response.json()
            links = [CuratedLink.from_json(link_data)
                     for link_data in links_data]
            return links
        else:
            response.raise_for_status()