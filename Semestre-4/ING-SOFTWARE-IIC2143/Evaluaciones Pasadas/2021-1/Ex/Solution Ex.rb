require 'json'

# Class with the responsibility of process contacts data
class ContactsProcesor
  LIMIT_AGE = 18

  def initialize (contacts) 
    @contacts = contacts
  end
  
  # Returns a contact's full name
  def get_full_name (contact)
    "#{contact["name"]} #{contact["last_name"]}"
  end

  # Creates a dictionary where the key is the contact's id,
  # and the value the contact's full name
  def get_names
    names = {}
    @contacts.each do |contact|
      names[contact["id"]] = get_full_name(contact)
    end
    return names
  end

  # Returns the contacts in the format required
  def parsed_contacts
    data = []
    names = get_names()
    @contacts.each do |contact|
      friends = []
      contact["friends"].each do |friend_id|
        friends.push(names[friend_id])
      end
      data.push({
        full_name: get_full_name(contact),
        age: contact["age"],
        full_age: contact["age"] >= LIMIT_AGE,
        friends: friends
      })
    end
    return data
  end
end

# Class with the responsibilities of calling the API
# and returning the right data.
class ContactsService
  BASE_URL = 'https://internalapidata.todosOnline.com'
  STAGE = 'dev'
  
  def initialize (endpoint) 
    @endpoint = endpoint
  end
  
  def construct_url (page)
    return "#{BASE_URL}/#{STAGE}/#{@endpoint}?page=#{page}"
  end
  
  # Calls the API
  def fetch_contacts (token, page)
    url = construct_url(page)
    headers = { "Accept" => "application/json", "Authentication" => "Bearer #{token}"}
    
    raw_response = HTTParty.get(url, headers)
    JSON.parse(raw_response)
  end

  # Returns the formated data
  def get_contacts (token)
    data = []
    for i in 1..2 do
      contacts = fetch_contacts(token, i)
      contact_processor = ContactsProcesor.new(contacts)
      data.concat(contact_processor.parsed_contacts)
    end
    return data
  end
end

