// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

contract PropertyTrackingSystem {
 
    // Property structure
    struct Property {
        uint propertyId;
        string location;
        uint size;
        address owner;
        bool isRegistered;
    }

    // Mapping to store properties by ID
    mapping(uint => Property)  properties;

  
    // Function to register a new property
    function registerProperty(uint id,string memory _location, uint _size) public {
        require(!properties[id].isRegistered);
        
        // Create new property
            properties[id] = Property({
            propertyId: id,
            location: _location,
            size: _size,
            owner: msg.sender,
            isRegistered: true
        });

      
    }

    // Function to transfer ownership of a property
    function transferOwnership(uint id, address _newOwner) public {
        // Ensure property is registered
        require(properties[id].isRegistered, "Property is not registered");

        // Ensure the sender is the current owner
        require(properties[id].owner == msg.sender, "Only the owner can transfer ownership");

        // Transfer ownership
        properties[id].owner = _newOwner;

    }

    // Function to get property details by ID
    function getPropertyDetails(uint id) public view returns (Property memory ) {
        // Ensure property is registered
        require(properties[id].isRegistered, "Property is not registered");

        return properties[id];
    }
}
